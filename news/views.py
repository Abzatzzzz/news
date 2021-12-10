from django.shortcuts import render, redirect, get_object_or_404
from .models import News, Category
from .forms import AddNewsCreateForm


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    return render(request, 'news/index.html', {'news': news, 'categories': categories})

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'news/category.html', {'news': news, 'categories': categories})

def get_news(request, news_id):
    return render(request, 'news/news_detail.html', {'news': get_object_or_404(News, pk=news_id)})

def add_news(request):
    if request.method == 'POST':
        form = AddNewsCreateForm(request.POST)
    form = AddNewsCreateForm()
    return render(request, 'news/add_news.html', {'form': form})

