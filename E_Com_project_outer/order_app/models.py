from django.db import models

# Create your models here.

class order_details(models.Model):
    order_no = models.CharField(max_length = 50)
    user_id = models.CharField(max_length = 50)
    product = models.CharField(max_length = 50)
    total_prise = models.CharField(max_length = 50)
    payment = models.CharField(max_length = 50)
    shypping_address = models.CharField(max_length = 50)
    order_status = models.CharField(max_length = 50)
    