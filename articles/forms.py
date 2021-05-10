from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'url', 'body', 'thumbnail']