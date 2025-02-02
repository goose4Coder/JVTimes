from django.urls import path, include
from . import views

urlpatterns = [
    path("all/", views.ArticleListView.as_view(), name='all-articles'),
    path("of_category/<int:pk>/", views.ArticleByCategoryListView.as_view(),name='article-of-category'),
    path("read/<int:pk>/", views.ArticleDetailView.as_view(),name='read-article'),
   
]
