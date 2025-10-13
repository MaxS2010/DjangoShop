from django.shortcuts import render

def render_user(request):
    return render(request, "user_app/user.html")
