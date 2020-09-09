from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article

def homepage(request):
    return render(request, 
                  'templates/pages/homepage.html')

def article(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request,
                  'templates/pages/article.html', context)
# Create your views here.
