from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post,Study
from django.contrib.auth.models import Group
from django.core.cache import cache

# Home


def home(request):
    # posts = Post.objects.all()
    posts = Study.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

# About


def about(request):
    return render(request, 'blog/about.html')

# Contact


def contact(request):
    return render(request, 'blog/contact.html')


def success(request):
    return render(request, 'blog/success.html')

# Dashboard


def dashboard(request):
    if request.user.is_authenticated:
        posts = Study.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip=request.session.get('ip',0)
        ct=cache.get('count',version=user.pk)
        return render(request, 'blog/dashboard.html', {'posts': posts, 'full_name': full_name, 'groups': gps,'ip':ip,'ct':ct})
    else:
        return HttpResponseRedirect('/login/')

# Logout


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Sigup


def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, 'Congratulations!! You have become an Author.')
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

# Login


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')

# Add New Post


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                url1 = form.cleaned_data['url1']
                url2 = form.cleaned_data['url2']
                url3 = form.cleaned_data['url3']
                url4 = form.cleaned_data['url4']
                image= form.cleaned_data['image']
                pst = Study(title=title, desc=desc,url1=url1,url2=url2,url3=url3,url4=url4,image=image)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

# Update/Edit Post


def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Study.objects.get(pk=id)
            form = PostForm(request.POST,request.FILES, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Study.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

# Delete Post


def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Study.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
