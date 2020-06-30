
from django.urls import path

from .views import LinkListView, \
    UserProfileDetailView, UserProfileUpdateView, LinkCreateView

app_name = 'core'

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('user/<slug>', UserProfileDetailView.as_view(), name='profile'),
    path('edit-profile/', UserProfileUpdateView.as_view(), name='edit_profile'),
    path('create-link/', LinkCreateView.as_view(), name='create_link')
]