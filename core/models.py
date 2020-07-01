from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Count
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.timezone import now


class Link(models.Model):
    title = models.CharField(max_length=250)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_on = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    votes_total = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:link_detail", kwargs={"pk": str(self.id)})


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)

    def __str__(self):
        return '%s upvotes %s' % (self.voter.username, self.link.title)


class Comment(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.commenter)

    def get_absolute_url1(self):
        return reverse("core:comment_detail", kwargs={"pk": str(self.id)})


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True)

    def __str__(self):
        return "%s's profile" % self.user


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)


# Signal while saving user
post_save.connect(create_profile, sender=User)
