from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from bookmark.models import Bookmark

from mysite.views import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
#--- ListView
class BookmarkLV(ListView):
    model = Bookmark

#--- DetailView
class BookmarkDV(DetailView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url', 'url_category']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form): # self.request
        form.instance.owner = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin, ListView):
    tempalte_name = "bookmark/bookmark_change_list.html"

    def get_queryset(self):
        return Bookmark.objects.filter(owner = self.request.user)

class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url', 'url_category']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')