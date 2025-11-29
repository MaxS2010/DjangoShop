from django.urls import path
from .views import render_author

urlpatterns = [
    path('author/<int:pk>', render_author, name= 'author_page')
]
