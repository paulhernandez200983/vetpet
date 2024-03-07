import numbers
from pyexpat import model
from re import M
from tkinter import PhotoImage
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Chicken1(models.Model):
    name = models.CharField(max_length=120)
    priceM= models.DecimalField(max_digits=8, decimal_places=2)
    priceL= models.DecimalField(max_digits=8, decimal_places=2)
    desc= models.CharField(max_length=120)
    address= models.CharField(max_length=120)
    tel= models.CharField(max_length=120)
    estd= models.CharField(max_length=120)
    pImage= models.URLField()
    datev=models.DateField()
    lat= models.DecimalField(max_digits=10, decimal_places=7)
    lon= models.DecimalField(max_digits=10, decimal_places=7)
    catg= models.CharField(max_length=120)
    rating=models.DecimalField(max_digits=4, decimal_places=2)
    puntos=models.SmallIntegerField()
  


class Burger1(models.Model):
    name = models.CharField(max_length=120)
    priceM= models.DecimalField(max_digits=4, decimal_places=2)
    priceL= models.DecimalField(max_digits=4, decimal_places=2)
    bImage= models.URLField()
   

class Drink1(models.Model):
    name = models.CharField(max_length=120)
    priceM= models.DecimalField(max_digits=4, decimal_places=2)
    priceL= models.DecimalField(max_digits=4, decimal_places=2)
    dImage= models.URLField()
    loc = models.CharField(max_length=120)

class Steak1(models.Model):
    name = models.CharField(max_length=120)
    priceM= models.DecimalField(max_digits=10, decimal_places=2)
    priceL= models.DecimalField(max_digits=10, decimal_places=2)
    sImage= models.URLField()
    loc = models.CharField(max_length=120)
    puntos=models.IntegerField()

class Pizza1(models.Model):
    name = models.CharField(max_length=120)
    priceM= models.DecimalField(max_digits=4, decimal_places=2)
    priceL= models.DecimalField(max_digits=4, decimal_places=2)
    zImage= models.URLField()
    loc = models.CharField(max_length=120)

from django.conf import settings
class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number = models.CharField(max_length=68)
    bill= models.DecimalField(max_digits=4, decimal_places=2)
    date= models.DateTimeField(auto_now_add=True, blank=True)
    note= models.TextField(blank=True,null=True)


class Items(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price= models.DecimalField(max_digits=4, decimal_places=2)
    size = models.CharField(max_length=68)


from django.db import models
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image_url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
   

class WishlistItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_image_url = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=200, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',  # Cambia este nombre a uno que prefieras
        related_query_name='custom_user_group'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',  # Cambia este nombre a uno que prefieras
        related_query_name='custom_user_permission'
    )


from django.conf import settings
from django.db import models

class Carrito(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    pollo = models.ForeignKey(Chicken1, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    
class procesar_pago(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ChickenReview(models.Model):
    chicken = models.ForeignKey('Chicken1', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=0, choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.chicken.name} by {self.user.username}"



from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()
class Order1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return f"Order {self.id} - Total: ${self.total_amount}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items1', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item {self.product_name} - Quantity: {self.quantity} - Price: ${self.price}"