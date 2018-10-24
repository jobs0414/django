from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = "blog/post_all.html" # psot_list.html
    context_object_name = "posts" # object_list

    paginate_by = 2

# post_detail.html
class PostDV(DetailView): # select * from where blog_post where slug=?
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'    