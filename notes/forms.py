from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            "title",
            "content",
            "is_public",
        )


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            "title",
            "content",
            "is_public",
        )
