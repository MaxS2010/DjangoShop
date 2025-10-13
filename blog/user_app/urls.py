from .views import render_user
from django.urls import path

urlpatterns = [
    path(
        route= 'profile/',
        view = render_user,
        name= "profile",
    )
]