from django.shortcuts import render
from .models import Post

def frontpage(request):
  post = Post.objects.all()
  return render(request, 'blog/frontpage.html', {"posts": post})
