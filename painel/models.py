from django.db import models

# ========================
#     CATEGORIAS
# ========================
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


# ========================
#      PRODUTOS
# ========================
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    main_image = models.ImageField(upload_to="products/main/")

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name

    @property
    def out_of_stock(self):
        return self.stock <= 0


# ========================
#  IMAGENS SECUNDÁRIAS
# ========================
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/gallery/")

    def __str__(self):
        return f"Imagem de {self.product.name}"
