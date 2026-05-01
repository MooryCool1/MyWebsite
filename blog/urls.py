from django.urls import path
from . import views

app_name = 'blog'  # ← این رو اضافه کن

urlpatterns = [
    path('', views.blog_view, name='index'),
    path('single/', views.blog_single, name='single'),
]