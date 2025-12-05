from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),
    
    # App de aprendices (incluida en la raíz para la página de inicio y otras rutas)
    path('', include('aprendices.urls')),
    
    # URLs de las otras apps, cada una con su propio prefijo
    path('instructores/', include('instructores.urls')),
    path('programas/', include('programas.urls')),
    path('cursos/', include('cursos.urls')),
]