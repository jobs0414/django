from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from cms.models import Book, Impression
from cms.forms import BookForm, ImpressionForm
<<<<<<< HEAD
from django.views.generic.list import ListView
=======
>>>>>>> 9e3938c344be5380c54385b01dfa4f6a0a867132

# Create your views here.
def book_list(request):
    # return HttpResponse('도서 목록')
    books = Book.objects.all().order_by('id')

    context = {}
    context['books'] = books

    return render(request, 'cms/book_list.html', context)

def book_edit(request, book_id=None):
    # return HttpResponse('도서 수정')
    
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()
    
    if request.method == 'POST': # POST
        # POST된 request 데이터를 가지고 Form 생성
        form = BookForm(request.POST, instance=book) 
        # save()
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list')

    else: # GET 
        # book instance에서 Form 생성
        form = BookForm(instance=book) 
        return render(request, 'cms/book_edit.html', dict(form=form, book_id=book_id))

def book_remove(request, book_id):
<<<<<<< HEAD
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('cms:book_list')

class ImpressionList(ListView):
    context_object_name = "impressions"
    template_name = "cms/impresssion_list.html"
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs["book_id"])
        impressions = book.impressions.all().order_by("id")
        self.object_list = impressions
        
        context = self.get_context_data(object_list=self.object_list, book=book)
        return self.render_to_response(context)

def impression_edit(request, book_id, impress_id=None):    
    return HttpResponse("감상평 수정/추가")

def impression_remove(request, book_id, impress_id):    
    return HttpResponse("감상평 삭제")    
=======
    return HttpResponse('도서 삭제')
>>>>>>> 9e3938c344be5380c54385b01dfa4f6a0a867132
