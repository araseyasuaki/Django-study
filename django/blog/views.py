from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from .forms import CommentForm

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blog/frontpage.html', {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=post.slug)

    return render(request, "blog/post_detail.html", {"post": post, "form": form})