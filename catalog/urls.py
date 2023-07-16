from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import contacts, pageNotFound, home

app_name  = CatalogConfig.name

urlpatterns = [

    path('', home, name='products'),
    path("contacts/", views.contacts, name="contacts/")

]

handler404 = pageNotFound
