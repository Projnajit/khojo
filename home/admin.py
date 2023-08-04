from django.contrib import admin

from . models import Posts


class PostsModel(admin.ModelAdmin):
    list_display=['location','rentfare','bedroom']

admin.site.register(Posts,PostsModel)
