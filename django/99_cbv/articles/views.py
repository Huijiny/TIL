from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Article
from django.views import View
# Create your views here.


class AboutView(TemplateView):
    template_name = 'articles/about3.html'


def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        context = {
            'articles': articles,
        }

        return render(request, 'articles/index.html', context)


class IndexView(View):
    def get(self, request):
        articles = Article.objects.all()
        context = {
            'articles': articles,
        }

        return render(request, 'articles/index2.html', context)


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'heejin'
        return context


class ArticleDetailView(DetailView):
    model = Article
    