from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import os
from django.template.loader import get_template
from django.template import engines

def blog_view(request, ** kwargs):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now()).order_by('-published_date')
    if kwargs.get('cat_name') != None:
        posts = posts. filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts. filter(author__username = kwargs['author_username' ])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
       
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)

def blog_single(request, pk):    
    post = get_object_or_404(Post, pk=pk, status=True, published_date__lte=timezone.now())
    post.counted_views += 1
    post.save()
    all_posts = list(Post.objects.filter(status=True, published_date__lte=timezone.now()))
    current_index = all_posts.index(post)
    previous_post = all_posts[current_index - 1] if current_index > 0 else None
    next_post = all_posts[current_index + 1] if current_index < len(all_posts) - 1 else None
    comments = Comment.objects.filter(post=post.id, approved=True).order_by('-created_date')
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
        'comments': comments
    }
    return render(request, "blog/blog-single.html", context)

# def blog_category(request, cat_name):
#     posts = Post.objects.filter(status=True)
#     posts = posts.filter(category__name=cat_name)
#     context = {'posts': posts}
#     return render(request, "blog/blog-home.html", context)

def blog_search(request):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    if request.method == 'GET':
        #print(request.GET.get('s'))
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)