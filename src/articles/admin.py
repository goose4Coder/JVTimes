from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = (
        'author',
    )
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
admin.site.register(models.Category)