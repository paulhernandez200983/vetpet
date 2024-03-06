from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True, help_text="Write a valid address")
    phone_number = forms.CharField(max_length=20, required=False, help_text="Enter your phone number")
    profile_image_url = forms.CharField(max_length=200, required=False)
    direccion=forms.CharField(max_length=200)
    estado=forms.CharField(max_length=200)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'date_joined', 'phone_number', 'profile_image_url', 'direccion', 'estado']


from django import forms
from .models import Chicken1

class AgregarPolloForm(forms.ModelForm):
    class Meta:
        model = Chicken1
        fields = '__all__'
class Payment(UserCreationForm):
    class Meta:
        
        fields = '__all__'