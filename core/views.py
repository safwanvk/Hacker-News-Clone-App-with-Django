from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView

from .forms import UserProfileForm, LinkForm, VoteForm
from .models import Link, UserProfile, Vote


class LinkListView(ListView):
    model = Link
    template_name = "core/link_list.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(LinkListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            voted = Vote.objects.filter(voter=self.request.user)
            links_in_page = [link.id for link in context["object_list"]]
            voted = voted.filter(link_id__in=links_in_page)
            voted = voted.values_list('link_id', flat=True)
            context["voted"] = voted

        return context


class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = 'username'
    template_name = "core/user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "core/edit_profile.html"

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)

    def get_success_url(self):
        return reverse('profile', kwargs={'slug': self.request.user})


class LinkCreateView(CreateView):
    model = Link
    form_class = LinkForm
    template_name = "core/create_link.html"

    def form_valid(self, form):
        f = form.save(commit=False)
        f.rank_score = 0.0
        f.submitter = self.request.user
        f.save()

        return super(LinkCreateView, self).form_valid(form)


class LinkDetailView(DetailView):
    model = Link
    template_name = "core/link_detail.html"


class LinkUpdateView(UpdateView):
    model = Link
    form_class = LinkForm
    template_name = "core/update_link.html"


class LinkDeleteView(DeleteView):
    model = Link
    template_name = "core/delete_link.html"
    success_url = '/'


class VoteFormView(FormView):
    model = Vote
    form_class = VoteForm
    template_name = "core/link_list.html"
    success_url = '/'

    def form_valid(self, form):
        link = get_object_or_404(Link, pk=form.data['link'])
        user = self.request.user
        prev_votes = Vote.objects.filter(voter=user, link=link)
        has_voted = (prev_votes.count() > 0)

        if not has_voted:
            # add vote
            Vote.objects.create(voter=user, link=link)
            link.votes_total += 1
            link.save()
            print('voted')
        else:
            # delete vote
            prev_votes[0].delete()
            link.votes_total -= 1
            link.save()
            print('unvoted')

        return redirect('/')

    def form_invalid(self, form):
        print('invalid')
        return redirect('/')
