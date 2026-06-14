from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField
from django_summernote.widgets import SummernoteWidget
from .models import Post


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post title'}),
            'content': SummernoteWidget(),
            'category': forms.CheckboxSelectMultiple(),
        }