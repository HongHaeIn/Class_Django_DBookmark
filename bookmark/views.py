from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from bookmark.models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark
    #bookmark_list.html, {'boookmark_list': Bookmark.objects.all()}

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name', 'url']  #'__all__'
    #bookmark_form.html -> bookmark_create.html
    template_name_suffix = '_create'
    success_url = reverse_lazy('bookmark:list')
