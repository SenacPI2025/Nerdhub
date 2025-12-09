from django.urls import path
from .views import index
from . import views

app_name = "nucleo"

urlpatterns = [
    path('', index, name='index'),
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('sobre/', views.sobre, name='sobre'),
    path('suporte/', views.suporte, name='suporte'),
    path('marca/<slug:marca_slug>/', views.produtos_por_marca, name='produtos_por_marca'),
    path('produto/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
]