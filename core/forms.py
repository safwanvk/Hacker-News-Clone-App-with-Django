from django import forms

from .models import UserProfile, Link, Vote, Comment


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ['submitter', 'votes_total']


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'
        exclude = ['voter', 'link']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']