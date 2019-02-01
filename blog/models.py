from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    article_title = models.CharField(max_length = 200)
    article_content = models.TextField()
    author = models.CharField(max_length = 200)
    post_date = models.DateTimeField('date published')
    views = models.IntegerField(default = 0)

    def __str__(self):
        return self.article_title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    comment = models.CharField(max_length = 250)
    author = models.CharField(max_length = 200)
    post_date = models.DateTimeField('date published')

    def __str__(self):
        return self.comment
