from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class neighbourhood(models.Model):
    neighbourhood= models.CharField(max_length=100)

    def __str__(self):
        return self.neighbourhood

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()



class Profile(models.Model):
    profpic = models.ImageField(upload_to='profpics/',null=True)
    description = HTMLField(null=True)
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE,null=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name =models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=150,null=True)
    image = models.ImageField(upload_to='post/',null=True)
    post = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood= models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    profpic = models.ImageField(upload_to='profpics/',null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=300 ,null=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,null=True)

class Business(models.Model):
    logo = models.ImageField(upload_to='logos/',null=True)
    description = HTMLField(null= True)
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE,null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name =models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    address =models.CharField(max_length=100,null=True)
    contact = models.IntegerField(null= True)

    def __str__(self):
        return self.name
    

class healthservices(models.Model):
    healthservices = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.healthservices

    def save_healthservices(self):
        self.save()

    @classmethod
    def delete_healthservices(cls,healthservices):
        cls.objects.filter(healthservices=healthservices).delete()

class Health(models.Model):
    logo = models.ImageField(upload_to='healthlogo/',null=True)
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)
    healthservices = models.ManyToManyField(healthservices)

    def __str__(self):
        return self.name

class Authorities(models.Model):
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE,null=True)
    name =models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    contact = models.IntegerField(null=True)
    address =models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
    

class notifications(models.Model):
    title = models.CharField(max_length=100,null=True)
    notification = HTMLField(null=True)
   
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE,null=True)
    post_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
