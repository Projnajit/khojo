from django.contrib.auth.models import User
from django.forms import fields
from django.shortcuts import render, redirect
from login import models
from django.http import HttpResponse
from django.contrib import messages
from .forms import userform
from django.contrib.auth.hashers import make_password


def f1(request):
    form = userform()
    if request.method == 'POST':
        form = userform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            User.objects.create(
                username=form.cleaned_data['name'], password=make_password(form.cleaned_data['pasw']))
            user = form.cleaned_data.get('name')
            messages.success(
                request, "Account Created Successfully For " + user)
            return redirect('login')
        else:
            messages.error(request, "Please Fill Out All Fields Correctly")
    return render(request, 'signup.html', {'form': form})
