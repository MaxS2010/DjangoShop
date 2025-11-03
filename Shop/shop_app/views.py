from django.shortcuts import render

def render_shop(req):
    return render(
        request= req,
        template_name= 'shop_app/shop.html',
        context= {
            "products": [
                {"name": "Ноутбук Lenovo IdeaPad 3",     "price": 18999.00, "in_stock": True},
                {"name": "Смартфон Samsung Galaxy A35",  "price": 13499.00, "in_stock": True},
                {"name": "Навушники Sony WH-CH520",      "price": 2999.00,  "in_stock": False},
                {"name": "Монітор LG 24MP400",           "price": 5299.00,  "in_stock": True},
                {"name": "Мишка Logitech M185",          "price": 599.00,   "in_stock": True},
            ]
        }
    )

def render_main(req):
    return render(
        request= req,
        template_name= 'shop_app/main.html',
    )