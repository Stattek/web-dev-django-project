from django.db import models


# Create your models here.
class WikiPage(models.Model):
    description = models.CharField(max_length=20000)
    image_url = models.CharField(max_length=200, default="default_image.jpg")
    last_edited = models.DateTimeField(verbose_name="Time Page Was Last Edited")


class Skill(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='img', default="default_image.jpg")
    type = models.CharField(max_length=200)  # if it is passive or active
    element = models.CharField(max_length=200)
    casting_time = models.DecimalField(verbose_name="Seconds to Cast", max_digits=10, decimal_places=2)
