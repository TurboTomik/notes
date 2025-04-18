from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from notes.models import Note

from .forms import NoteForm


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
        "notes": notes
    }
    return render(request, "notes/my-notes.html", context)
    