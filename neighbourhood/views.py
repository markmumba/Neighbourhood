
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *


# Create your views here.
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)

    return render(request, 'profile.html', {'profile': profile})


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('project_all')
    else:
        form = ProfileForm()

    return render(request, 'new-profile.html', {"form": form})
@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('Index')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'update_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def blog(request):
    current user = request.user
    profile=Profile.objects.get(username=current_user)
    blog = Blog.objects.filter(neighbour=profile.neighbourhood)
    
    return render (request,'blog.html',{'blog':blog})

@login_required(login_url='/accounts/login/')
def new_blog(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit = False)
            blog.username = current_user
            blog.neighbourhood = profile.neighbourhood
            blog.profile_image = profile.profile_image
            blog.save()

        return HttpResponseRedirect('blog')

    else:
        form = BlogForm()

    return render(request,'blog_form.html',{"form":form})
