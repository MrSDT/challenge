from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    url = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):  # For Getting Post Title and Put it in Admin Article Page
        return self.title

    def short_description(self):  # For Showing 100 Character of Text in main article page
        return self.body[:100] + '...'

    def thumbnail_def(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return "\media\default.jpg"
