from django.db import models

class Post(models.Model):
    # img
    # author
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tags
    #category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField()
    published_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)