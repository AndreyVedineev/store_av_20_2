from django.core.management import BaseCommand

from catalog.models import Product
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        pk_1 = Category.objects.get(pk=1)
        pk_2 = Category.objects.get(pk=2)
        pk_3 = Category.objects.get(pk=3)
        pk_4 = Category.objects.get(pk=4)

        product_list = [
            {'name': 'Сушки', 'category': pk_1, 'price': 5.50},
            {'name': 'Сарделька', 'category': pk_2, 'price': 34.40},
            {'name': 'Амур белый', 'category': pk_3, 'price': 1200.00}
        ]
        # for item in product_list:
        #     Product.objects.create(**item)

        product_for_create = []
        for item in product_list:
            product_for_create.append(
                Product(**item)
            )
        Product.objects.bulk_create(product_for_create)
