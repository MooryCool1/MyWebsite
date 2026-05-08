from django.urls import path
from . import views
app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
   # path('blog/', views.blog_home, name='blog_home'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
]
