from django.shortcuts import render, redirect, get_object_or_404
from .models import News, Category
from .forms import AddNewsCreateForm

from django.views.generic import CreateView, ListView, DetailView

class IndexListView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    #extra_context = {'title': 'Главная страница'} #нежелательный способ

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategoryListView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):  # it is supposed to be filtering data in db
        return News.objects.filter(category=self.kwargs['category_id'], is_published=True)


class GetNewsDetailView(DetailView):
    """
     джанго не требует обьявления template_name если название шаблона имеет формат 'view'+'название апликейшна' в данном случа view_news.html 
    """
    model = News
    context_object_name = 'news'
    #pk_url_kwarg = 'news_id' # возможный способ передачи pk

class CreateNewsView(CreateView):
    form_class = AddNewsCreateForm
    template_name = 'news/add_news.html'

