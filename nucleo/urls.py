from django.urls import path
from .views import index

app_name = "nucleo"

urlpatterns = [
    path('', index, name='index'),
]
