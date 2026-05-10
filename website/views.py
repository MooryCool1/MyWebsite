from django.shortcuts import render

def index(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')


def blog_single(request):
    return render(request, 'blog/blog-single.html') 