from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 모든 게시글을 조회

    # 1. DB로부터 받은 쿼리셋을 이후에 파이썬이 정렬 변경 (python이 조작)
    # articles = Article.objects.all()[::-1]

    # 2. 처음부터 원하는 정렬로 된 쿼리셋을 받음 (DB가 조작)
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# 하나의 view함수가 request의 method에 따라서 2가지 역할을 하게 됨.
def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # POST가 아닌 다른 method
    else:
        form = ArticleForm()
    context = {
        # 상황에 따른 2가지 모습
        # 1. is_valid에서 내려온 form:
        # 2. else에서 내려온 form - 빈 폼
        'form': form,
    }
    return render(request, 'articles/create.html', context)



def detail(request, pk):
    # 몇번 글을 조회할건지 가져와야 함
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    # 삭제할 게시글 조회
    article = Article.objects.get(pk=pk)
    # 삭제 요청이 POST면 삭제, POST가 아니라면 DETAIL 페이지로 redirect
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def update(request, pk):
    article = Article.objects.get(pk=pk) 
    # update
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
