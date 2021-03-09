from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('image/', views.image, name='image')
]
