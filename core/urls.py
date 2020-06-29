
from django.urls import path

from . views import LinkListView

app_name = 'core'

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list')

]