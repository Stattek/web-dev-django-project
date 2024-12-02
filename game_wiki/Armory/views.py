
from django.shortcuts import render
from .models import Weapon, Armor

def index(request):
    weapons = Weapon.objects.all()
    armors = Armor.objects.all()
    return render(request, 'Armory/index.html', {'weapons': weapons, 'armors': armors})
