from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.template import loader

from .models import Article

def index(request):
    articles = Article.objects.order_by('-post_date')
    return render(request, 'blog/index.html', {'articles': articles})

def article(request, title):
    article = get_object_or_404(Article, article_title = title)
    return render (request, 'blog/article.html', {'article': article})