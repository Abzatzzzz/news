from django.urls import path

from . import views


app_name = "news"

urlpatterns = [
    path('', views.IndexListView.as_view(), name="home"),
    path('category/<int:category_id>', views.NewsByCategoryListView.as_view(extra_context={'title': 'category_unknown'}), name="category"),
    path('<int:pk>', views.GetNewsDetailView.as_view(), name='news_detail'),
    path('add_news/', views.CreateNewsView.as_view(), name='add_news'),
]
