from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views
from .views import register
from .views import update_cart_quantity
from .views import cart_view

urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('login/', auth_views.LoginView.as_view(template_name='urbanApp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('cart/', cart_view, name='cart_view'),  
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),  
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'), 
    path('cart/update/<int:product_id>/', update_cart_quantity, name='update_cart_quantity'),
    path('cart/clear/', clear_cart, name='clear_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('checkout/', views.checkout, name='checkout'),  # Ruta para la página de checkout
    path('checkout/complete/', views.checkout_complete, name='checkout_complete'),  # Ruta para completar el checkout
    path('checkout/thank-you/', views.checkout_thank_you, name='checkout_thank_you'),  # Ruta para la página de agradecimiento
    ]