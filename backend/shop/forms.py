from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Product, User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available','stock','category']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Product name'}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
            'available': forms.CheckboxInput(),
            'stock' : forms.NumberInput(attrs={'placeholder': 'Stock'}),
            'category': forms.Select(),
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('Price must be greater than 0')
        return price

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

