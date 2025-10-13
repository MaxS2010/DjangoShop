from django.shortcuts import render

def render_post(request):
    return render(request, "post_app/post.html")
