from tkinter.font import names
from django.urls import path

from . import views

app_name = "entry"
urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("skills", views.skills_page, name="skills_page"),
    path("skills/<int:page_id>", views.wiki_page, name="wiki_page"),
    path("skills/add_skill", views.add_skill, name="add_skill"),
    path("skills/<int:skill_id>/delete_skill", views.delete_skill, name="delete_skill"),
]
