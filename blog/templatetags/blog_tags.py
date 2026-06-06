from django import template
from django.utils import timezone
from blog.models import Post
from blog.models import Category
register = template.Library()

@register.inclusion_tag('blog/blog-popular-post.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-post-category.html')
def postcategories():
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('website/latest-posts.html')
def latestblogposts(arg=6):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-tags.html')
def posttags():
    from taggit.models import Tag
    tags = Tag.objects.all()
    return {'tags': tags}