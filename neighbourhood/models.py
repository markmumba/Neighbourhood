from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.




class Neighbourhood(models.Model):
    neighbourhood = models.CharField(max_length=100)

    def __str__(self):
        return self.neighbourhood

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls, neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()



class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile/', null=True)
    user = models.TextField(null=True)
    neighbourhood=models.ForeignKey(Neighbourhood,null=True,on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True)



    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()





class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='post/')
    post = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood= models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    profile_image= models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.title

class Business(models.Model):
    picture=models.ImageField(upload_to='picture/')
    description=HTMLField()
    neighbourhood=models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address =models.CharField(max_length=120)

    def __str__(self):
        return self.name
        

