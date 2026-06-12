from django import template
from django.utils import timezone
from blog.models import Post, Category, Comment
from django.db.models import Count, Q

register = template.Library()


@register.inclusion_tag('blog/blog-popular-post.html')
def latestposts(arg=3):
    posts = Post.objects.filter(
        status=True,
        published_date__lte=timezone.now()
    ).only('title', 'image', 'published_date', 'pk').order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-category.html')
def postcategories():
    categories = Category.objects.annotate(
        post_count=Count('post', filter=Q(post__status=True))
    )
    return {'categories': categories}


@register.simple_tag(name='comments_count')
def function(pk):
    return Comment.objects.filter(post=pk, approved=True).count()


@register.inclusion_tag('website/latest-posts.html')
def latestblogposts(arg=6):
    posts = Post.objects.filter(
        status=True,
        published_date__lte=timezone.now()
    ).only('title', 'image', 'published_date', 'pk').order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-tags.html')
def posttags():
    from taggit.models import Tag
    tags = Tag.objects.all()
    return {'tags': tags}