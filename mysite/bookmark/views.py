from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Create your views here.
#--- ListView
class BookmarkLV(ListView):
    # object_list 
    # views.py -> template (xxxx_list.html)
    model = Bookmark

#--- DetailView
class BookmarkDV(DetailView):
    # object
    # views.py -> template (xxxx_detail.html)
    model = Bookmark