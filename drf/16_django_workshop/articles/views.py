from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def articles_list(request):
    articles = get_list_or_404(Article)
    if request.method == 'GET':
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'{ article_pk }'
        }
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)