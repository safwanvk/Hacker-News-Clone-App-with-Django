from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .forms import UserProfileForm, LinkForm
from .models import Link, UserProfile


class LinkListView(ListView):
    model = Link
    template_name = "core/link_list.html"
    queryset = Link.with_votes.all()
    paginate_by = 3


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
