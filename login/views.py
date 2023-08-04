from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import users
from home.models import Posts
 
 
def f1(request):
    Post = Posts.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        uz = authenticate(request,username=username, password=password)
        if uz is not None:
            login(request,uz)
            id = users.objects.filter(name=username).values('id')[0]['id']
            return redirect('home',id)
        else:
            messages.error(request,"Wrong Credentials")
    return render(request,'login.html')




