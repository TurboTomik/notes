from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserSignupForm


def sign_up(request):
    if request.method == "POST":
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("core:index"))
    else:
        form = UserSignupForm()

    context = {
        "form": form,
    }

    return render(request, "users/signup.html", context)
