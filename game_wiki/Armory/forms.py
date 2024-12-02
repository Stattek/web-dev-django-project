from django import forms
from .models import Weapon, Armor

class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ['name', 'description', 'attack_power', 'weapon_type']

class ArmorForm(forms.ModelForm):
    class Meta:
        model = Armor
        fields = ['name', 'description', 'defense_power', 'armor_type']
