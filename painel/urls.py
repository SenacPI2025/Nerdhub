from django.urls import path
from . import views

app_name = 'painel'

urlpatterns = [
    path('login/', views.login_painel, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_painel, name='logout'),
    path('', views.dashboard, name='dashboard'),

    path('produtos/', views.produtos_list, name='produtos_list'),
    path('produtos/novo/', views.produto_novo, name='produto_novo'),
    path('produtos/<int:id>/editar/', views.produto_editar, name='produto_editar'),

    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('pedidos/', views.pedidos_list, name='pedidos_list'),
]