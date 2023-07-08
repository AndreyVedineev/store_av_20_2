from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    print(request.POST)
    return render(request, 'catalog/contacts.html')

