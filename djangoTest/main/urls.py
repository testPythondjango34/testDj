from main import views
from django.urls import path
urlpatterns = [
    path('', views.mainPage, name='mainPage' )
]
