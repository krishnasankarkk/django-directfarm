from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('shop/', views.shop, name='Shop'),
    path('about/', views.about, name='About'),
    path('farmers/', views.farmers, name='Farmers'),
    path('contact/', views.contact, name='Contact'),
]
