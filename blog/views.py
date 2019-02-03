from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import CommentForm
from .models import Article, Comment

def index(request):
    articles = Article.objects.order_by('-post_date')
    return render(request, 'blog/index.html', {'articles': articles})

def article(request, pk):
    article = get_object_or_404(Article, pk = pk)
    return render (request, 'blog/article.html', {'article': article})

def add_comment(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'article.html', {'article': article})