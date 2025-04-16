from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path("create-note/", views.create_note, name="create-note"),
]
