from tkinter.font import names
from django.urls import path

from . import views

app_name = "entry"
urlpatterns = [
    path("", views.table_of_contents, name="table_of_contents"),
    path("<int:page_id>", views.wiki_page, name="wiki_page"),
]
