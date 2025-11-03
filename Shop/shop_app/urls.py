from django.urls import path
from shop_app.views import render_shop

urlpatterns = [
    path('products/', render_shop, name= 'products'),
]
