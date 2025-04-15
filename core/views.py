from django.shortcuts import render

def index(request):
    context = {
        "title": "Home - Notes",
    }
    return render(request, "core/index.html", context)
