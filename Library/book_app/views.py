from django.shortcuts import render, get_object_or_404
from .models import Book 

# Create your views here.
def render_home(request):
    book_list = Book.objects.all()
    return render(
        request= request,
        template_name= 'book_app/home.html',
        context={'books': book_list}
        )

def render_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # book = Book.objects.get(pk = pk)
    return render(
        request= request,
        template_name= 'book_app/book.html',
        context={'book': book}
    )