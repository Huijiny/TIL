from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2. 
    article = Article(title=title, content=content)
    # 데이터 검증
    article.save()

    # 3.
    # Article.objects.create(title=title, content=content)
    context = {
        'title': title,
        'content': content,
    }

    return render(request, 'articles/create.html', context)