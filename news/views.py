from django.shortcuts import render, redirect, get_object_or_404
from .models import News, Category
from .forms import AddNewsCreateForm

from django.views.generic import CreateView, ListView

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

    def get_queryset(self):
        return News.objects.filter(category=self.kwargs['category_id'], is_published=True)


def get_news(request, news_id):
    return render(request, 'news/news_detail.html', {'news': get_object_or_404(News, pk=news_id)})

def add_news(request):
    if request.method == 'POST':
        form = AddNewsCreateForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect('news:home')


    form = AddNewsCreateForm()
    return render(request, 'news/add_news.html', {'form': form})

