
from django import forms

class BookingForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        label="Full Name", 
        widget=forms.TextInput(attrs={
            'class': 'block w-96 px-3 py-2 rounded-md border shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'autocomplete': 'name'
        })
    )
    email = forms.EmailField(
        label="Email Address", 
        widget=forms.EmailInput(attrs={
            'class': 'block w-96 px-3 py-2 rounded-md border shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'autocomplete': 'email'
        })
    )
    phone = forms.CharField(
        max_length=15, 
        label="Phone Number", 
        widget=forms.TextInput(attrs={
            'class': 'block w-96 px-3 py-2 rounded-md border shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'autocomplete': 'tel'
        })
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'block w-96 h-24 px-3 py-2 rounded-md border shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'autocomplete': 'street-address'
        }), 
        label="Address"
    )
    driver_license = forms.CharField(
        max_length=300, 
        label="Driver's License", 
        widget=forms.TextInput(attrs={
            'class': 'block w-96 px-3 py-2 rounded-md border shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'autocomplete': 'off'
        })
    )
    cnic = forms.CharField(
        max_length=15, 
        label="CNIC", 
        widget=forms.TextInput(attrs={
            'class': 'block w-96 px-3 py-2 rounded-md border shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'autocomplete': 'off'
        })
    )
    start_date = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={
            'type': 'date', 
            'class': 'block w-96 px-3 py-2 rounded-md border shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'autocomplete': 'off'
        })
    )
    return_date = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={
            'type': 'date', 
            'class': 'block w-96 px-3 py-2 rounded-md border shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            'autocomplete': 'off'
        })
    )
    car_name = forms.CharField(
        max_length=200, 
        widget=forms.HiddenInput()
    )
    car_company = forms.CharField(
        max_length=200, 
        widget=forms.HiddenInput()
    )
    car_image = forms.URLField(
        widget=forms.HiddenInput()
    )
    car_price = forms.CharField(
        max_length=200,
        widget=forms.HiddenInput()
    )

