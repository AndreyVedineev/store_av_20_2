from django.http import HttpResponseNotFound
from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Продукты'
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)

        # print(request.POST)
    return render(request, 'catalog/contacts.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
