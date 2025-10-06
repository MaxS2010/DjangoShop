from django.contrib import admin
from django.urls import path, include

import User

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', User.index),
    path('user/', include("User.urls")),
    path('posts/', include("Posts.urls")),
]
