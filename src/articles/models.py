from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Article(models.Model):
    title = models.CharField('Title',max_length=60)
    description = models.CharField('Description',max_length=300, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    creation_date = models.DateTimeField(auto_now=True, verbose_name="creation_date")
    content = CKEditor5Field('Content', config_name='default')
    def __str__(self):
        return self.title
    @property
    def author_name(self):
        return self.author.first_name +" "+ self.author.last_name