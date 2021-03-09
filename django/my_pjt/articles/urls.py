from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('image/', views.image, name='image'),
    path('search/', views.search, name='search'),
    path('result/<int:param1>/<int:param2>/', views.result, name='result'),
    path('dtl-practice', views.dtl_practice, name='dtl_practice'),
]
