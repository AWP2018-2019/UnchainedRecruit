from django import forms
from Recruit import models

class RecuiterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    e_mail = forms.CharField(max_length=100)
    class Meta:
        model = models.Recruiter

class AngajatForm(forms.ModelForm):
'''class AnuntForm(forms.ModelForm):
    class Meta:
        model = models.Anunt
        fields = ['text']'''

class AnuntForm(forms.ModelForm):
    class Meta:
        model = models.Anunt
        fields = ['descriere','titlu']

'''class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    e_mail = forms.CharField(max_length=100)
    class Meta:
        model = models.Angajat
        model =models.UserProfile
        exclude = ['user', 'friend_requests', 'friends']'''
        model =models.UserProfile
        exclude = ['user', 'friend_requests', 'friends']'''
