from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from notes.models import Note

from .forms import NoteForm, EditNoteForm


@login_required(login_url="/user/sign-in")
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("core:index")
    else:
        form = NoteForm()

    context = {
        "title": "Create Note - Notes",
        "form": form,
    }
    return render(request, "notes/create-note.html", context)


@login_required(login_url="/user/sign-in")
def my_notes(request):
    notes = Note.objects.filter(user_id=request.user.id)
    context = {
        "title": "My Notes - Notes",
        "notes": notes,
    }
    return render(request, "notes/my-notes.html", context)


@login_required(login_url="/user/sign-in")
def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user_id=request.user.id)
    if request.method == "POST":
        form = EditNoteForm(data=request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes:edit-note", note_id)
    else:
        form = EditNoteForm(instance=note)

    context = {
        "title": "Edit Note - Notes",
        "form": form,
    }
    return render(request, "notes/edit-note.html", context)
