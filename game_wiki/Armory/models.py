from django.db import models

# Create your models here.
class Weapon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="No description available")
    attack_power = models.IntegerField()
    weapon_type = models.CharField(max_length=50)  # Example: 'Sword', 'Bow', etc.

    def __str__(self):
        return self.name


class Armor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="No description available")
    defense_power = models.IntegerField()
    armor_type = models.CharField(max_length=50)  # Example: 'Helmet', 'Chestplate', etc.

    def __str__(self):
        return self.name