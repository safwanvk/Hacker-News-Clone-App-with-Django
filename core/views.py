from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView


from .forms import UserProfileForm
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


