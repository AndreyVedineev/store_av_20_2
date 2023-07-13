from django.shortcuts import render
from django.http import HttpResponseNotFound


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)

    # print(request.POST)
    return render(request, 'catalog/contacts.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
