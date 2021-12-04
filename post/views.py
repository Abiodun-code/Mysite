from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Entry

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class NewsListView(ListView):
    model = Entry
    template_name = 'news.html'
    context_object_name = 'all_entry_list'

class NewsDetailView(DetailView):
    model = Entry
    template_name = 'detail.html'

class NewsCreateView(CreateView): 
    model = Entry
    template_name = 'create.html'
    fields = ['entry_title', 'entry_text', 'entry_author']
