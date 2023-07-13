from django.urls import path

from catalog import views
from catalog.views import home, contacts, pageNotFound

urlpatterns = [

    path('', home),
    path("contacts", views.contacts, name="contacts/")

]

handler404 = pageNotFound
