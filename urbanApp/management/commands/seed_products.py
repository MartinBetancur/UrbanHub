from django.core.management.base import BaseCommand
from urbanApp.models import Product
import factory
from faker import Faker

fake = Faker()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    price = factory.Faker('random_number', digits=5)
    description = factory.Faker('sentence')

class Command(BaseCommand):
    help = 'Seed the database with products'

    def handle(self, *args, **kwargs):
        for _ in range(10):
            ProductFactory.create()
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with products'))