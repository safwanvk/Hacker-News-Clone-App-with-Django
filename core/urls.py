
from django.urls import path

from .views import LinkListView,\
    UserProfileDetailView

app_name = 'core'

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('user/<slug>', UserProfileDetailView.as_view(), name='profile')

]