from django.urls import path
from website.views import *
from blog.views import *
app_name = 'website'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog-single/', blog_single, name='blog_single'),
    path('contact/', contact, name='contact'),
    path('newsletter', newsletter_view ,name='newsletter')
]
