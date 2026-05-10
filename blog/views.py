from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
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