from django.contrib import admin
from django.db import models
from .models import users

class codersModel(admin.ModelAdmin):
    list_display=['name','phone','address']


admin.site.register(users,codersModel)
# Register your models here.
