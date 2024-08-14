from django.shortcuts import render
from .models import Post

def frontpage(request):
  post = Post.objects.all()
  return render(request, 'blog/frontpage.html', {"posts": post})

def post_detail(request, slug):
  post = Post.objects.get(slug=slug)
  return render(request, "blog/post_detail.html", {"post": post})
