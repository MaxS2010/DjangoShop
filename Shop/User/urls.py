from django.urls import path

import User

urlpatterns = [
    path('profile/', User.index, name='profile'),
]