from django.shortcuts import render

def create_note(request):
    return render(request, "notes/create-note.html")
