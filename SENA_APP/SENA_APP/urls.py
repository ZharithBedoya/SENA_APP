from django.contrib import admin
from django.urls import path,include
from aprendices import views
from instructores import views
from programas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aprendices.urls')),
    path("",include('instructores.urls')),
    path("",include('programas.urls'))
]
