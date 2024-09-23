from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Variation(models.Model):
    product = models.ForeignKey(Product, related_name='variations', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Nombre de la variación (por ejemplo, Color o Tamaño)
    value = models.CharField(max_length=100)  # El valor de la variación (por ejemplo, Rojo o M)
    extra_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.name}: {self.value} (+${self.extra_price})'