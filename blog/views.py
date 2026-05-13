from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
def blog_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    if cat_name:    
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username = author_username)
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
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
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