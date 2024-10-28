from django.db import models
from django.contrib.auth.models import AbstractUser
from customer_app.manager import CustomUserManager
from django.utils.translation import gettext_lazy

# Create your models here.

class custom_user(AbstractUser):
     username = None
     name = models.CharField(max_length = 50, unique = True)
     mobile = models.IntegerField(null = True, blank = True) #This need to be set null if you dont want it to be in required fields
     email = models.EmailField( max_length=254, unique = True)
     address = models.CharField(max_length = 250, null = True, blank = True) #This need to be set null if you dont want it to be in required fields
     
     USERNAME_FIELD = 'name'
     REQURED_FIELD = 'email' 
     objects = CustomUserManager()
     
     def __str__(self):
          return self.name