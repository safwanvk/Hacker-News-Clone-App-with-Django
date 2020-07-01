from django import forms

from .models import UserProfile, Link, Vote


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
        exclude = ['submitter']


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'
        exclude = ['voter', 'link']
