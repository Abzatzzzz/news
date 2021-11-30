from django.urls import path

from . import views


app_name = "news"

urlpatterns = [
    path('', views.index, name="home"),
    path('category/<int:category_id>', views.get_category, name="category"),
    path('<int:news_id>', views.get_news, name='news_detail'),
]
