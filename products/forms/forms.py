from django import forms
from products.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter brand'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter model'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter year'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter color'}),
            'mileage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter mileage'}),
            'is_new': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
