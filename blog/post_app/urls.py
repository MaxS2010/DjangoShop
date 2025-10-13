from .views import render_post
from django.urls import path

urlpatterns = [
    path(
        route= 'show/',
        view= render_post,
        name= "post",
        
    ),

]
