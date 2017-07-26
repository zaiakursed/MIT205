# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Spec(models.Model):
    specification=models.CharField(max_length=200)
    measure = models.DecimalField(max_digits=30, decimal_places=15)
    unit=models.CharField(max_length=30)
   
# ...
    def __str__(self):
      
        return self.specification

class Brand(models.Model):
    brand_name=models.CharField(max_length=50)
    website=models.CharField(max_length=50)

# ...
    def __str__(self):
      
        return self.brand_name


class Category(models.Model):
    category_name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)

# ...
    def __str__(self):
      
        return self.category_name

class Supplier(models.Model):
    supplier_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=50)

# ...
    def __str__(self):
      
        return self.supplier_name


class Price(models.Model):
    wholesale_price =models.CharField(max_length=50)
    retail_price =models.CharField(max_length=50)
 

# ...
    def __str__(self):
      
        return self.retail_price

class Item(models.Model):
    spec=models.ForeignKey(Spec, on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price=models.ForeignKey(Price, on_delete=models.CASCADE)
    item_name=models.CharField(max_length=50)
    stock_in = models.DecimalField(max_digits=30, decimal_places=15, default=0.0)
    stock_out = models.DecimalField(max_digits=30, decimal_places=15, default=0.0)
    total_stock = models.DecimalField(max_digits=30, decimal_places=15, default=0.0)
    exclude = ('total_stock')
# ...
    def __str__(self):
      
        return self.item_name

