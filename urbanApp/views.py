from django import forms
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.shortcuts import redirect, get_object_or_404, render
from .models import Product, Variation
from django.http import JsonResponse


# Create your views here.

#Registro
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Esto guarda el usuario en la base de datos
            login(request, user)  # Inicia sesión al usuario recién registrado
            return redirect('home')  # Redirige al home o a la página que desees
    else:
        form = UserRegisterForm()
    return render(request, 'urbanApp/register.html', {'form': form})


#Login 
def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/login')
        else:
            messages.error(request, 'Login failed. Please check your credentials.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

#Logout
def custom_logout_view(request):
    logout(request)
    return redirect('/logout')


# Agregar productos al carrito

def add_to_cart(request, product_id):
    # Asegúrate de que la solicitud es POST, de lo contrario redirige
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)

    product = get_object_or_404(Product, id=product_id)

    # Obtener la variación seleccionada si existe
    variation_id = request.POST.get('variation')
    
    if variation_id:
        variation = get_object_or_404(Variation, id=variation_id, product=product)
        variation_name = f'{variation.name}: {variation.value}'
        variation_price = float(product.price) + float(variation.extra_price)
    else:
        variation_name = 'Sin variación'
        variation_price = float(product.price)

    cart = request.session.get('cart', {})

    # Generar una clave única para el producto (considerar variación si aplica)
    cart_key = f'{product_id}:{variation_id}' if variation_id else str(product_id)

    if cart_key in cart:
        cart[cart_key]['quantity'] += 1
    else:
        cart[cart_key] = {
            'name': product.name,
            'variation': variation_name,
            'price': str(variation_price),
            'quantity': 1
        }

    # Guardar el carrito en la sesión
    request.session['cart'] = cart

    # Manejar solicitudes AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Verificar si es una solicitud AJAX
        total_quantity = sum(item['quantity'] for item in cart.values())
        total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
        
        # Renderizar el contenido del carrito como HTML
        try:
            cart_html = render(request, 'urbanApp/cart_content.html', {'cart': cart}).content.decode('utf-8')
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

        return JsonResponse({'success': True, 'total_quantity': total_quantity, 'cart_html': cart_html})

    return redirect('cart_view')

# Eliminar productos del carrito
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]  # Eliminar el producto del carrito
        request.session['cart'] = cart  # Actualizar el carrito en la sesión

    return redirect('cart_view')

# Ver el contenido del carrito
def cart_view(request):
    cart = request.session.get('cart', {})
    total = sum(float(item['price']) * item['quantity'] for item in cart.values())  # Calcular total
    return render(request, 'urbanApp/cart.html', {'cart': cart, 'total': total})

#Actualizar cantidades
def update_cart_quantity(request, product_id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))

    if str(product_id) in cart and quantity > 0:
        cart[str(product_id)]['quantity'] = quantity
        request.session['cart'] = cart

    return redirect('cart_view')

#Vaciar el carrito
def clear_cart(request):
    request.session['cart'] = {}  # Limpiar el carrito
    return redirect('cart_view')

#checkout
def checkout(request):
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())

    context = {
        'cart': cart,
        'total_price': total_price
    }
    return render(request, 'urbanApp/checkout.html', context)


##checkout compelto
def checkout_complete(request):
    if request.method == 'POST':
        # Aquí procesarías la información de pago (aún no implementado)
        # Por ahora, simplemente vaciamos el carrito y redirigimos a una página de agradecimiento.

        # Vaciar el carrito después de la compra
        request.session['cart'] = {}
        
        return redirect('checkout_thank_you')
    
    return redirect('checkout')

def checkout_thank_you(request):
    return render(request, 'urbanApp/thank_you.html')
#clases
class HomePageView(TemplateView):
    template_name = 'urbanApp/home.html'
    
class AboutPageView(TemplateView):
    template_name = 'urbanApp/about.html'
    

class ProductListView(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'

class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Product
    template_name = 'products/show.html'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

class ProductCreateView(LoginRequiredMixin,View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        return render(request, self.template_name, {'form': form})