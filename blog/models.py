from django.db import models
from datetime import datetime

class Article(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
