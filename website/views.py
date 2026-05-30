from django.shortcuts import render
from django.http import *
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages
def index(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_obj = form.save(commit=False)
            contact_obj.name = 'Unknown'
            contact_obj.subject = contact_obj.subject or ''  
            contact_obj.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submited successfuly')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket didnt submited')

    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})
def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def blog_single(request):
    return render(request, 'blog/blog-single.html') 