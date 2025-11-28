from django.contrib import path
from aprendices import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.aprendices, name=''),
    path ('aprendices/', views.aprendices, name='aprendices'),
]