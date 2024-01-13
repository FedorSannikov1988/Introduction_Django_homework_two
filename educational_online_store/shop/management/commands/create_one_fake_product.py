from decimal import Decimal
from shop.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create one fake product"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name fake product')
        parser.add_argument('description', type=str, help='Description fake product')
        parser.add_argument('price', type=str, help='Price fake product')
        parser.add_argument('quantity', type=int, help='Quantity fake product')

    def handle(self, *args, **kwargs):

        name: str = kwargs.get('name')
        description: str = kwargs.get('description')
        price: str = kwargs.get('price')
        decimal_price: Decimal = Decimal(price)
        quantity: int = kwargs.get('quantity')

        one_product = \
            Product(name=name,
                    description=description,
                    price=decimal_price,
                    quantity=quantity)

        self.stdout.write(str(one_product))

        one_product.save()
