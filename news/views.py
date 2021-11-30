from django.shortcuts import render, redirect
from . models import News, Category


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    return render(request, 'news/index.html', {'news': news, 'categories': categories})

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'news/category.html', {'news': news, 'categories': categories})

def get_news(request, news_id):
    return render(request, 'news/news_detail.html', {'news': News.objects.get(pk=news_id)})
