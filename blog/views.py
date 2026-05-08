from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)

def blog_single(request, pk):
    post = get_object_or_404(Post, pk=pk, status=True)
    post.counted_views += 1
    post.save()
    context = {'post': post}
    return render(request, "blog/blog-single.html", context)