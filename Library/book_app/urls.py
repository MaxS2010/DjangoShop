from django.urls import path
from .views import render_home, render_book

urlpatterns = [
    path('', render_home),
    path('book/<int:pk>', render_book, name="book_url")
]