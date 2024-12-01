from django.db import models


# Create your models here.
class WikiPage(models.Model):
    description = models.CharField(max_length=20000)
    image_url = models.CharField(
        max_length=200, default="default_image.jpg"
    )  # TODO: add default image
    last_edited = models.DateTimeField(verbose_name="Time Page Last Edited")


class Skill(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200, default="default_image.jpg")
    type = models.CharField(max_length=200)  # if it is passive or active
    casting_time = models.DecimalField(verbose_name="Seconds to Cast")
    element = models.CharField(max_length=200)
