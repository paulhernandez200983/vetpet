from django.contrib import admin
from .models import  Chicken1
from .models import Burger1
from .models import Pizza1
from .models import Steak1
from .models import Drink1
from .models import Order
from .models import Items
from .models import CustomUser
from django.contrib.auth.models import AbstractUser
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class Chicken1Admin(ImportExportModelAdmin):
    list_display= ('name', 'priceM', 'priceL', 'catg', 'estd')
admin.site.register(Chicken1, Chicken1Admin)


class Burger1Admin(admin.ModelAdmin):
    list_display= ('name', 'priceM', 'priceL')
admin.site.register(Burger1, Burger1Admin)


class Pizza1Admin(admin.ModelAdmin):
    list_display= ('name', 'priceM', 'priceL', 'loc')
admin.site.register(Pizza1, Pizza1Admin)


class Drink1Admin(admin.ModelAdmin):
    list_display= ('name', 'priceM', 'priceL', 'loc')
admin.site.register(Drink1, Drink1Admin)


class Steak1Admin(admin.ModelAdmin):
    list_display= ('name', 'priceM', 'priceL', 'loc' )
admin.site.register(Steak1, Steak1Admin)

class OrderAdmin(admin.ModelAdmin):
    list_display= ('customer', 'number', 'bill')
admin.site.register(Order, OrderAdmin)


class ItemsAdmin(admin.ModelAdmin):
    list_display= ('order', 'name', 'size')
admin.site.register(Items, ItemsAdmin)

from .models import CustomUser


from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import CustomUser

class CustomUserAdmin(ImportExportModelAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'phone_number', 'direccion', 'estado')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'direccion', 'estado')
    list_filter = ('date_joined', 'estado')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'profile_image_url', 'direccion', 'estado')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'profile_image_url', 'direccion', 'estado'),
        }),
    )

# Registra la clase CustomUserAdmin con el modelo CustomUser
admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib import admin
from .models import Carrito, ItemCarrito, ChickenReview

admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(ChickenReview)
