from django.urls import path

import Posts

urlpatterns = [
    path('posts/', Posts.index, name='posts'),
]