from django.shortcuts import get_object_or_404, render, redirect
from books.forms import BookForm
from django.urls import reverse
from books.models import Book
from django.contrib.auth.decorators import login_required

@login_required(login_url='books:login')
def create(request):
    form_action = reverse('books:create')
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
         }
        if form.is_valid:
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('books:update', book_id = book.pk)


        return render(request, 'books/create.html', 
                  context)


    context = {
        'form': BookForm(),
        'form_action': form_action

    }
    return render(request, 'books/create.html', 
                  context)


@login_required(login_url='books:login')
def update(request, book_id):
    book = get_object_or_404(Book, pk=book_id, show=True, owner=request.user)
    form_action = reverse('books:update', args=(book_id,))
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        context = {
            'form': form,
            'form_action': form_action,
         }
        if form.is_valid:
            book = form.save()
            return redirect('books:update', book_id = book.pk)


        return render(request, 'books/create.html', 
                  context)


    context = {
        'form': BookForm(instance=book),
        'form_action': form_action

    }
    return render(request, 'books/create.html', 
                  context)


@login_required(login_url='books:login')
def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id, show=True, owner=request.user)
    confirmation = request.POST.get('confirmation', 'no')
    if confirmation == 'yes':
        book.delete()
        return redirect('books:index')

    return render(
        request, 
        'books/book.html',
        {
            'book': book,
            'confirmation': confirmation
        })