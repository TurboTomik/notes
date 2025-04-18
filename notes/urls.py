from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path("create-note/", views.create_note, name="create-note"),
    path("my-notes/", views.my_notes, name="my-notes"),
    path("edit-note/<int:note_id>/", views.edit_note, name="edit-note"),
]
