from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User 
# from jigyaasa.settings import STATIC_ROOT
# from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=255)
    phone =  models.CharField(max_length=13)
    email =  models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message from '+self.name+"-"+self.email


class Comment(models.Model):

    sno= models.AutoField(primary_key=True)
    comment2=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    # parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    # post=models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp= models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.comment2[0:8] + "..." + "by" + " " + self.user.username


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=255)
    title = models.CharField(max_length=20)
    # likes = models.IntegerField(default=0)
    comment= models.ForeignKey(Comment, on_delete=models.CASCADE,blank=True,null=True)
    question = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return f"Post from {self.name} - {self.timeStamp}"


class upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)                     
    profile_pic = models.FileField(upload_to='image')
    # default="", upload_to=STATIC_ROOT

    def __str__(self):
        return   "image" + "by" + " " + self.user.username