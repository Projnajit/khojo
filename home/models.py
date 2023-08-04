from distutils.command.upload import upload
from django.db import models
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField
# Create your models here.


class Posts(models.Model):
    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Postss'
    usid = models.CharField(max_length=255,null=True,blank=True)
    postid = models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=1040)
    area = models.CharField(max_length=255)
    rentfare = models.IntegerField()
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    parking = models.CharField(max_length=255)
    contactnumber = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    photo1 = models.ImageField(null=True,blank=True)
    photo2 = models.ImageField(null=True,blank=True)
    photo3 = models.ImageField(null=True,blank=True)
    photo4 = models.ImageField(null=True,blank=True)
    photo5 = models.ImageField(null=True,blank=True)
    added = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.location)
    class Meta:
     ordering = ['-added']

    

 