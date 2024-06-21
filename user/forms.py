from django import forms
from .models import UserCar

class UserCarSubmissionForm(forms.ModelForm):
    class Meta:
        model = UserCar
        fields = [
            'full_name', 'email', 'phone', 'cnic', 'address',
            'car_name', 'car_company', 'category', 'engine', 'car_description', 'image'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Tailwind CSS classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'appearance-none border rounded-lg w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
            field.widget.attrs['placeholder'] = field.label
            field.label = False
            
            
        self.fields['car_description'].widget.attrs['style'] = 'height: 100px;'