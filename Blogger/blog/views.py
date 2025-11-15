from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

# Create your views here.

def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content, published_at=timezone.now())
        return redirect('home')
    return render(request, 'blog/add_post.html')