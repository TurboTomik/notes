from django.shortcuts import render

def index(request):
    context = {
        "title": "Home - Notes",
        "index_page": True,
    }
    return render(request, "core/index.html", context)
