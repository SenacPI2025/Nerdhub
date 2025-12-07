from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nucleo.urls')),
    path('painel/', include('painel.urls', namespace='painel')),
]

# Manipuladores de erro personalizados
handler404 = 'nucleo.views.custom_404'
handler500 = 'nucleo.views.custom_500'