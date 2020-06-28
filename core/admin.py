from django.contrib import admin

# Register your models here.
from .models import Link, Vote

admin.site.register(Link)
admin.site.register(Vote)