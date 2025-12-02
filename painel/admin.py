from django.contrib import admin
from .models import Product, Category, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "stock", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("name",)
    inlines = [ProductImageInline]


admin.site.register(Category)
admin.site.register(ProductImage)
