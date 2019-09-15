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


class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class NeighbourHood(models.Model):
    name = models.CharField(max_length=40)
    location = models.ForeignKey(Location, on_delete==models.CASCADE)
    occupants=models.IntegerField(null=True, default=0)
    
    def __str__(self):
        return self.name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neigborhood_id):
        neighborhood = cls.objects.get(id = neigborhood_id)
        return neighborhood

    def update_neighborhood(self):
        self.save()

    def update_occupants(self):
        self.occupants += 1
        self.save()
