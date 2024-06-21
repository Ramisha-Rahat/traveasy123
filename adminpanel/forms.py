from django import forms
from cars.models import Car
from adminpanel.models import AdminUsers

from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-black font-bold placeholder-gray-400 focus:outline-none focus:border-blue-500',
                'placeholder': 'Enter car name'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-black font-bold placeholder-gray-400 focus:outline-none focus:border-blue-500',
                'placeholder': 'Enter price'
            }),
            'daily_rental_price': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-black font-bold placeholder-gray-400 focus:outline-none focus:border-blue-500',
                'placeholder': 'Enter daily rental price'
            }),
            'reviews': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-black font-bold placeholder-gray-400 focus:outline-none focus:border-blue-500',
                'placeholder': 'Enter reviews'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-black font-bold placeholder-gray-400 focus:outline-none focus:border-blue-500',
                'placeholder': 'Enter description',
                'rows': 3
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-black font-bold placeholder-gray-400 focus:outline-none focus:border-blue-500'
            }),
            'company': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-black font-bold placeholder-gray-400 focus:outline-none focus:border-blue-500',
                'placeholder': 'Enter company'
            }),
            'fuel_type': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-black font-bold placeholder-gray-400 focus:outline-none focus:border-blue-500',
                'placeholder': 'Enter fuel type'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-black font-bold focus:outline-none focus:border-blue-500'
            }),
        }


class AdminLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'appearance-none border rounded-lg w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(attrs={
            'class': 'appearance-none border rounded-lg w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Password'
            })
    )