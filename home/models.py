from django.db import models
from .managar import *
from django.contrib.auth.models import AbstractUser,PermissionsMixin





class CustomUser(AbstractUser,PermissionsMixin):


    username = None
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length = 12)
    is_phone_no_verified = models.BooleanField(default=False)
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    user_type = models.CharField(max_length=10, choices=ROLE_CHOICES,default=ROLE_CHOICES[0])
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']    # 
    


class NoticeBoard(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    notice = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=100)
    


    def __str__(self):
        return self.notice
    
