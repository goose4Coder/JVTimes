from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . import models

class ArticleListView(ListView):
    model = models.Article
    queryset = models.Article.objects.order_by("-creation_date")
    context_object_name = "articles"

class ArticleDetailView(DetailView):
    model = models.Article
    