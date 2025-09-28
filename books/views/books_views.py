from django.shortcuts import get_object_or_404, render, redirect
from books.models import Book
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    books =Book.objects.filter(show=True).order_by('-id')

    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_tittle': 'Livros - '
    }
    return render(request, 'books/index.html', 
                  context)


def book(request, book_id):
    single_book = get_object_or_404(Book, pk=book_id, show=True) 
    book_name = single_book.title
    context = {
        'book': single_book,
        'site_tittle': f'{book_name} - '  
    }
    return render(request, 'books/book.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('books:index')
    
    books = Book.objects.filter(show=True).filter(
        Q(title__icontains=search_value) | 
        Q(author__icontains=search_value)
        )
    
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_tittle': 'Livros - '
    }
    return render(request, 'books/index.html', 
                  context)
    
    