from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django import http
from login.models import users
from django.shortcuts import render, redirect
from django.http import HttpResponse
from signup.forms import Postform
from . models import Posts
import string
import random
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .filters import Postfilter

from home.models import Posts

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))

usrid="4"

@login_required(login_url='login')
def func(request, users_id):
    global usrid
    usrid=users_id
    Post = Posts.objects.all()
    profile = users.objects.get(id=users_id)
    myfilter = Postfilter(request.GET,queryset=Post)
    Post = myfilter.qs
    
    context = {'profile': profile,'Post':Post ,'myfilter':myfilter}
    return render(request, 'home.html', context)


@login_required(login_url='login')
def spost(request,posts_id):
    profile = users.objects.get(id=usrid)
    str = Posts.objects.filter(postid=posts_id).values('location')[0]['location']
    str1 = "https://maps.google.com/maps?q=" + str + "%20&t=&z=13&ie=UTF8&iwloc=&output=embed"
    print(str1)
    Post = Posts.objects.get(postid=posts_id)
    context = {'Post': Post,'cod':usrid,'profile': profile,'gmp':str1}
    return render(request, 'spost.html', context)

@login_required(login_url='login')
def manage(request,users_id):
    profile = Posts.objects.filter(usid=users_id)
    context = {'cod':usrid,'profile': profile}
    return render(request, 'manage.html', context)

@login_required(login_url='login')
def update(request,posts_id):
    Post = Posts.objects.get(postid=posts_id)
    context = {'Post':Post,'cod':usrid}
    if request.method=='POST':
        form = Postform(request.POST or None,request.FILES or None,instance=Post)
        if form.is_valid():
            form.save()
            return redirect('home',usrid)
        else:
            print(form.errors.as_data())
            
    return render(request, 'update.html', context)

@login_required(login_url='login')
def delete(request,posts_id):
    HttpResponse("HELLO 1234")
    Post = Posts.objects.get(postid=posts_id)
    Post.delete()
    return redirect('manage',usrid)

    

def lgout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def abt(request,users_id):
    profile = users.objects.get(id=users_id)
    context={'user':users,'cod':users_id,'profile': profile}
    return render(request,'about.html',context)

@login_required(login_url='login')
def ren(request,users_id):
    form = Postform()
    pid = id_generator()
    context={'user':users,'form':form,'cod':users_id,'pid':pid}
    if request.method=='POST':
        form = Postform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home',users_id)
        else:
            print(form.errors.as_data())
        
    return render(request,'addpost.html',context)
 