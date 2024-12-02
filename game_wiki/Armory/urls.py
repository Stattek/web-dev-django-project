from django.urls import path
from . import views

app_name = 'Armory'

urlpatterns = [
    path('', views.index, name='index'),  # Home page of the Armory app
    path('add_weapon/', views.add_weapon, name='add_weapon'),  # URL for adding weapons
    path('add_armor/', views.add_armor, name='add_armor'),  # URL for adding armor
    path('remove_weapon/<int:weapon_id>/', views.remove_weapon, name='remove_weapon'),
    path('remove_armor/<int:armor_id>/', views.remove_armor, name='remove_armor'),
    ]