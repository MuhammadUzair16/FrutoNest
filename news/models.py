from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name




class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    content = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return f'Comment by {self.name} on {self.article}'
