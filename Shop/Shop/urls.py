from django.contrib import admin
from django.urls import path, include
from shop_app import render_main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_main),
    path('shop/', include('shop_app.urls'))
]
