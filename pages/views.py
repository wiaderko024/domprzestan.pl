from django.shortcuts import render
from posts.models import Post


def home_page(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
