# Generated by Django 5.1.3 on 2024-12-02 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Armory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='armor',
            name='description',
            field=models.TextField(default='No description available'),
        ),
        migrations.AddField(
            model_name='weapon',
            name='description',
            field=models.TextField(default='No description available'),
        ),
    ]