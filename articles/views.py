from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms


def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    return render(request, 'articles/articles.html', {'articles': articles})


def articles_in(request, url):
    inarticle = models.Article.objects.get(url=url)
    return render(request, 'articles/posts.html', {'inpost': inarticle})


@login_required(login_url='/accounts/login')
def create_post(request):
    if request.method == 'POST':
        cpost = forms.CreatePost(request.POST,request.FILES)
        if cpost.is_valid:
            instance = cpost.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        cpost = forms.CreatePost()
        return render(request, 'articles/createpost.html', {'cpost': cpost})