from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Product, User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'available']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']