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
    rank_score = models.FloatField(default=0.0)
    url = models.URLField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    votes_total = models.IntegerField(default=0)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:link_detail", kwargs={"pk": str(self.id)})

    def set_rank(self):
        # Based on HN ranking algo at http://amix.dk/blog/post/19574

        SECS_IN_HOUR = float(60 * 60)
        GRAVITY = 1.2

        delta = now() - self.submitted_on
        item_hour_age = delta.total_seconds() // SECS_IN_HOUR
        votes = self.votes - 1
        self.rank_score = votes / pow((item_hour_age + 2), GRAVITY)
        self.save()


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)

    def __str__(self):
        return '%s upvotes %s' % (self.voter.username, self.link.title)


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
