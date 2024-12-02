from django.contrib import admin
from .models import Weapon, Armor

class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'attack_power', 'weapon_type')
    search_fields = ('name',)

class ArmorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'defense_power', 'armor_type')
    search_fields = ('name',)

admin.site.register(Weapon)
admin.site.register(Armor)