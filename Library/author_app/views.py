from django.shortcuts import render

# Create your views here.

def render_author(request):
    return render(request, 'author_app/author.html')