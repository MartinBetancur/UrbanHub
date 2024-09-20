from django import forms

from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.views import View


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'urbanApp/home.html'
    
class AboutPageView(TemplateView):
    template_name = 'urbanApp/about.html'
    

class ProductListView(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/show.html'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

class ProductCreateView(View):
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