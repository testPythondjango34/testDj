from django.contrib import admin
from django.urls import path,include
from main import urls, views

urlpatterns = [
    path('', include('main.urls') ),
     path('admin/', admin.site.urls),
]
