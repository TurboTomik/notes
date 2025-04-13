from django.shortcuts import render


def sign_up(request):
    return render(request, "users/signup.html")
