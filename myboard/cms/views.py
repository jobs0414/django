from django.shortcuts import render
from django.http import HttpResponse

from cms.models import Book

# Create your views here.
def book_list(request):
    # return HttpResponse('도서 목록')
    books = Book.objects.all().order_by('id')

    context = {}
    context['books'] = books

    return render(request, 'cms/book_list.html', context)

def book_edit(request, book_id=None):
    return HttpResponse('도서 수정')

def book_remove(request, book_id):
    return HttpResponse('도서 삭제')