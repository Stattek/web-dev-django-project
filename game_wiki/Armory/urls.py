from django.urls import path
from . import views

app_name = 'Armory'

urlpatterns = [
    path('', views.index, name='index'),  # Home page of the Armory app
]