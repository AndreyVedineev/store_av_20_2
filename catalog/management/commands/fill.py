from django.core.management import BaseCommand
from django.core.management.color import no_style
from django.db import connection

from catalog.models import Category
from catalog.models import Product

sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Category, Product])
with connection.cursor() as cursor:
    for sql in sequence_sql:
        cursor.execute(sql)


class Command(BaseCommand):

    def handle(self, *args, **options):

        category_list = [
            {'name': 'Хлебобулочные изделия', 'description': 'Хлеб: ржаной, пшеничный, ржано-пшеничный, '
                                                             'пшенично ржаной всех видов'},
            {'name': 'Рыбные продукты', 'description': 'Рыба и продукты из рыбы'},
            {'name': 'Мясные продукты', 'description': 'Мясо и продукты из мяса'},
            {'name': 'Молочные продукты', 'description': 'Молоко и продукты из молока'}
        ]
        category_for_create = []
        for item in category_list:
            category_for_create.append(
                Category(**item)
            )
        Category.objects.bulk_create(category_for_create)

        pk_1 = Category.objects.get(pk=1)
        pk_2 = Category.objects.get(pk=2)
        pk_3 = Category.objects.get(pk=3)
        pk_4 = Category.objects.get(pk=4)

        product_list = [
            {'name': 'Сушки', 'category': pk_4, 'price': 5.50},
            {'name': 'Сарделька', 'category': pk_2, 'price': 34.40},
            {'name': 'Амур белый', 'category': pk_3, 'price': 1200.00},
            {'name': 'Кефир', 'category': pk_1, 'price': 45.00}
        ]
        # for item in product_list:
        #     Product.objects.create(**item)

        product_for_create = []
        for item in product_list:
            product_for_create.append(
                Product(**item)
            )
        Product.objects.bulk_create(product_for_create)
