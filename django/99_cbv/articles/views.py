from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    # fields = '__all__'
    fields = ('title',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = '__all__'


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:index')