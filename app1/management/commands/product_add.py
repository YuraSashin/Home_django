from random import randint
from django.core.management.base import BaseCommand, CommandParser
from app1.models import Product

class Command(BaseCommand):
    help = 'Create products'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('count', type=int, default=1, help='Number of products')

    def handle(self, *args, **options) -> None:
        count = options['count']
        for i in range(1, count + 1):
            product = Product(
                title=f'Product {i}',
                description=f'Description of product {i}',
                price=1500.00,
                count=randint(1, 15),
            )
            self.stdout.write(self.style.SUCCESS(f'Added order: {product}'))
            product.save()