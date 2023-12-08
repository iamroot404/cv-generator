from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    price = models.IntegerField()
    product_image = models.ImageField(upload_to='photos/products')
    info = models.CharField(max_length=200, default='Personal Information')
    career = models.CharField(max_length=200, blank=True)
    education = models.CharField(max_length=200, default='Educational Background')
    work = models.CharField(max_length=200, blank=True)
    skills = models.CharField(max_length=200, default='Skills And Hobbies')
    ref = models.CharField(max_length=200, default='Referee')
    link = models.CharField(max_length=200, default='basic')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_premium = models.BooleanField(default=True)


    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)




    def __str__(self):
        return self.product_name