from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.shortcuts import redirect
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("articles/", include("articles.urls")),
    path("", (lambda request: redirect("all-articles")), name='articles'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
