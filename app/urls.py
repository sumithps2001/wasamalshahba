from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('single/product/', views.singleproduct, name='single-product'),
    path('contact/', views.contact, name='contact'),
]
