from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

 


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image_path = models.CharField(max_length=200)
     
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.
    CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='products')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
         


    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='categories')

    def __str__(self):
        return self.name

   



        

    

