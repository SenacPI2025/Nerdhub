from django.urls import path
from .views import index

app_name = "nucleo"

urlpatterns = [
    path('', index, name='index'),
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),

]

