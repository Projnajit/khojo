from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from login.models import users
from home.models import Posts
from django import forms


class userform(ModelForm):
    class Meta:
            model = users
            fields= '__all__'
            
class Postform(ModelForm):
    class Meta:
            model = Posts
            fields= '__all__'

        






