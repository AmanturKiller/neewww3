from django import forms
from django.contrib.auth.models import User
from .models import *


class DatePicker(forms.DateInput):
    input_type = 'date'


class ProductForm(forms.ModelForm):
    guarantee = forms.DateField(
        widget=DatePicker,
        label="Последний день гарантии",
        required=False,
    )
    
    expiration_date = forms.DateField(
        widget=DatePicker,
        label="Последний день срока годности",
        required=False,
    )
    
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'qty',
            'category',
            'guarantee',
            'expiration_date'
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'password', 
            'first_name', 
            'last_name'
        ]
    
class AuthForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
