
from django.shortcuts import render, get_object_or_404, redirect
from .models import Weapon, Armor
from .forms import WeaponForm, ArmorForm

def index(request):
    weapons = Weapon.objects.all()
    armors = Armor.objects.all()
    return render(request, 'Armory/index.html', {'weapons': weapons, 'armors': armors})

# View for adding a weapon
def add_weapon(request):
    if request.method == "POST":
        form = WeaponForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Armory:index')  # Redirect to the armory page after saving
    else:
        form = WeaponForm()
    return render(request, 'Armory/addweapon.html', {'form': form})

# View for adding an armor
def add_armor(request):
    if request.method == "POST":
        form = ArmorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Armory:index')  # Redirect to the armory page after saving
    else:
        form = ArmorForm()
    return render(request, 'Armory/addarmor.html', {'form': form})

# Remove Weapon
def remove_weapon(request, weapon_id):
    weapon = get_object_or_404(Weapon, id=weapon_id)
    weapon.delete()
    return redirect('Armory:weapon_list')  # Redirect to the list page after deletion

# Remove Armor
def remove_armor(request, armor_id):
    armor = get_object_or_404(Armor, id=armor_id)
    armor.delete()
    return redirect('Armory:armor_list')  # Redirect to the list page after deletion