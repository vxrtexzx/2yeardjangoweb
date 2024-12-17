# persons/urls.py
from django.urls import path
from .views import add_person, persons_list, redirect_to_add_person

urlpatterns = [
    path('', persons_list, name='persons_list'),  # Define URL for persons list
    path('add/', add_person, name='add_person'),
    path('', persons_list, name='home'),  # Define view for the root URL
]
