from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<str:pk>/', views.detail, name='detail'),
    path('<str:pk>/update/', views.update, name='update'),
]
