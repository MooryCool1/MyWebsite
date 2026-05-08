from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='index'),
    path('<int:pk>/', views.blog_single, name='single'),
]