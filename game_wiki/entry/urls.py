from tkinter.font import names
from django.urls import path

from . import views

app_name = "entry"
urlpatterns = [
    path("", views.skills_page, name="skills_page"),
    path("<int:page_id>", views.wiki_page, name="wiki_page"),
]

