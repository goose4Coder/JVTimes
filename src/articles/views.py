from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . import models

class ArticleListView(ListView):
    paginate_by = 4
    model = models.Article
    queryset = models.Article.objects.order_by("-creation_date")
    context_object_name = "articles"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = models.Category.objects.all()[:5]
        return context
        
    
class ArticleByCategoryListView(ListView):
    model = models.Article
    queryset = models.Article.objects.order_by("-creation_date")
    paginate_by = 4
    context_object_name = "articles"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = models.Category.objects.all()[:5]
        return context
    def get_queryset(self):
        return models.Article.objects.order_by("-creation_date").filter(category_id=self.request.resolver_match.kwargs['pk'])

class ArticleDetailView(DetailView):
    model = models.Article
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = models.Category.objects.all()[:3]
        return context