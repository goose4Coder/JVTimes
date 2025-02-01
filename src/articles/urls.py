from django.urls import path, include
from . import views

urlpatterns = [
    path("all/", views.ArticleListView.as_view(), name='all-articles'),
    path("read/<int:pk>/", views.ArticleDetailView.as_view(),name='read-article'),
]
