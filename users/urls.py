from django.urls import path

from . import views


app_name = "users"

urlpatterns = [
    path("sign-up/", views.sign_up, name="sign-up"),
    path("sign-in/", views.sign_in, name="sign-in"),
    path("logout/", views.logout, name="logout"),
]
