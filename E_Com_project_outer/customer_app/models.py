from django.db import models
from django.contrib.auth.models import AbstractUser
from customer_app.manager import custom_userManager
# Create your models here.

class custom_user(AbstractUser):
     username = None
     name = models.CharField(max_length = 50, unique = True)
     mobile = models.IntegerField()
     email = models.CharField(max_length = 50)
     address = models.CharField(max_length = 250)
     
     USERNAME_FIELD = 'name'
     REQURED_FIELD = 'email' 
     objects = custom_userManager()