from django import forms
from .models import Product


class PostFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'image', 'user')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
        }
