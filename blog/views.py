from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm
from django.db import models
def blog_view(request, **kwargs):
    posts = Post.objects.filter(
        status=True,
        published_date__lte=timezone.now()
    ).select_related('author').prefetch_related('category', 'tags').order_by('-published_date')

    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    try:
        posts = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        posts = paginator.get_page(1)

    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)


def blog_single(request, pk):
    post = get_object_or_404(
        Post.objects.select_related('author').prefetch_related('category', 'tags'),
        pk=pk,
        status=True,
        published_date__lte=timezone.now()
    )

    if post.login_require and not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts:login'))

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'your comment submited successfuly')
            return redirect('blog:single', pk=pk)
        else:
            messages.add_message(request, messages.ERROR, 'your comment did not submited')
    else:
        form = CommentForm()

    Post.objects.filter(pk=pk).update(counted_views=post.counted_views + 1)

    previous_post = Post.objects.filter(
        status=True,
        published_date__lte=timezone.now(),
        published_date__lt=post.published_date
    ).order_by('-published_date').first()

    next_post = Post.objects.filter(
        status=True,
        published_date__lte=timezone.now(),
        published_date__gt=post.published_date
    ).order_by('published_date').first()

    comments = Comment.objects.filter(post=post.id,)

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
        'comments': comments,
        'form': form
    }
    return render(request, "blog/blog-single.html", context)


def blog_search(request):
    posts = Post.objects.none()

    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = Post.objects.filter(
                status=True,
                published_date__lte=timezone.now()
            ).filter(
                models.Q(title__icontains=s) | models.Q(content__icontains=s)
            ).select_related('author').prefetch_related('category', 'tags')

    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = True
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            messages.add_message(request, messages.SUCCESS, 'Your post was submitted successfully')
            return redirect('blog:single', pk=post.id)
    else:
        form = PostForm()

    return render(request, 'blog/create-post.html', {'form': form})