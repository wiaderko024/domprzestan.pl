from django.shortcuts import render
from .models import Post


def post_page(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'post_page.html', {'post': post})
