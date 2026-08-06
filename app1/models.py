from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# User=get_user_model()
# Create your models here.

class Category(models.Model):       # breakfast, dinner, lunch
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)    # cascade ley jun data snga relate garxa tyo delele vayo ki tyo ni delete hunxa  #(foreign key category)
    name=models.CharField(max_length=200)
    price=models.FloatField()
    image=models.ImageField(null =True, blank=True)
    
    def __str__(self):
        return self.name
    
class Table(models.Model):
    number=models.CharField(max_length=2)
    is_available=models.BooleanField(default=True)
    
    def __str__(self):
        return f"Table {self.number} - {self.is_available}"
    
class Order(models.Model): 
    STATUS_CHOICE =[ 
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('D', 'Delivered')
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE)   #(foreign key user)  1 to many reln
    quantity=models.IntegerField(null=True, blank=True)
    total_price=models.FloatField(null=True, blank=True)
    status=models.CharField(max_length=1, choices=STATUS_CHOICE, default='P')
    is_paid=models.BooleanField(default=False)
    
class OrderMenu(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)      #(foreign key order)
    menu=models.ForeignKey(Menu, on_delete=models.PROTECT)        #(foreign key menu)