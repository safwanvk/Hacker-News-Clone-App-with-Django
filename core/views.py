from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Link


class LinkListView(ListView):
    model = Link
    template_name = "link_list.html"
    queryset = Link.with_votes.all()
    paginate_by = 3

