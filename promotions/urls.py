from django.urls import path
from . import views

urlpatterns = [
    path('deal/', views.deal_of_the_month, name='deal_of_the_month'),
]
