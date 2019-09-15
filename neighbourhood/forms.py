from django import forms
from .models import *



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']


class BlogForm(froms.ModelForm):
    class Meta:
        model=Blog
        exclude=['username','neighbourhood','profile_image']