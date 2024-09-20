from django.urls import path
from .views import *

urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    ]