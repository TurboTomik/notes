from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

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
