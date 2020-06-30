from django import forms

from .models import UserProfile, Link


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user',)


class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = '__all__'
        exclude = ['submitter', 'vote_score']
