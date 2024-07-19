from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('article/<int:pk>/', views.news_detail, name='news_detail'),
    path('comment/', views.submit_comment, name='comment'),
]