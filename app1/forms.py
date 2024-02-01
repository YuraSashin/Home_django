from django import forms
from .models import Product

class ImageForm:
    pass

class ImageField:
    pass

class ProductForm(forms.ModelForm):
    photo = forms.ImageField()
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'photo']