from django import forms
from .models import Product, Category, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'sku', 'brand', 'model', 'category', 'price', 'stock', 
            'is_active', 'description', 'dimensions', 'weight', 'materials', 
            'colors', 'main_features', 'package_contents', 'main_image'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm'}),
            'sku': forms.TextInput(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm'}),
            'brand': forms.TextInput(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm'}),
            'model': forms.TextInput(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm'}),
            'category': forms.Select(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm'}),
            'price': forms.NumberInput(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'toggle-switch active w-12 h-6 bg-primary rounded-full relative cursor-pointer'}),
            'description': forms.Textarea(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm resize-none', 'rows': 4}),
            'dimensions': forms.TextInput(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm'}),
            'weight': forms.NumberInput(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm', 'step': '0.01'}),
            'materials': forms.TextInput(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm'}),
            'colors': forms.TextInput(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm'}),
            'main_features': forms.Textarea(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm resize-none', 'rows': 4}),
            'package_contents': forms.Textarea(attrs={'class': 'w-full bg-[#2A2A2A] text-white px-4 py-3 rounded-lg border-none focus:outline-none focus:ring-2 focus:ring-primary text-sm resize-none', 'rows': 3}),
            'main_image': forms.FileInput(attrs={'class': 'hidden', 'id': 'imageUpload'}),
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'hidden'}),
        }