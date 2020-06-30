
from django.urls import path

from .views import LinkListView, \
    UserProfileDetailView, UserProfileUpdateView, LinkCreateView, LinkDetailView, LinkUpdateView

app_name = 'core'

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('user/<slug>', UserProfileDetailView.as_view(), name='profile'),
    path('edit-profile/', UserProfileUpdateView.as_view(), name='edit_profile'),
    path('create-link/', LinkCreateView.as_view(), name='create_link'),
    path('link-detail/<pk>', LinkDetailView.as_view(), name='link_detail'),
    path('update-link/<pk>', LinkUpdateView.as_view(), name='update_link'),

]