from django.db import models


# Create your models here.


class WikiPage(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=20000)
    
    def __str__(self) -> str:
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="img", default="default_image.jpg")
    type = models.CharField(max_length=200)  # if it is passive or active
    element = models.CharField(max_length=200)
    casting_time = models.DecimalField(
        verbose_name="Seconds to Cast", max_digits=10, decimal_places=2
    )
    wiki_page = models.ForeignKey(WikiPage, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
