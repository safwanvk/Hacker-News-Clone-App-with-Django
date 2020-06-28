from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Link(models.Model):
    title = models.CharField(max_length=250)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_on = models.DateTimeField(auto_now_add=True)
    vote_score = models.FloatField(default=0.0)
    url = models.URLField(max_length=250, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
