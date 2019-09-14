from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile/', null=True)
    user = models.TextField(null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
