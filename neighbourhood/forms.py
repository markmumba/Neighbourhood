 
from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']
        

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Blog
        exclude=['username','neighbourhood','profpic']

    
class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','neighbourhood']