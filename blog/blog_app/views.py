from django.shortcuts import render

def render_blog(request):
    return render(request, "blog_app/blog.html")
