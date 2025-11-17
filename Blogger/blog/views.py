from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def home(request):
    posts = Post.objects.all()
    
    return render(request, 'blog/home.html', {'posts': posts})

def add_post(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')

        Post.objects.create(title=title, content=content, image=image, published_at=timezone.now())
        
        return redirect('home')
   
    return render(request, 'blog/add_post.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    return render(request, 'blog/post_detail.html', {'post': post})

def update_post(request, post_id):
    
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        
        post.title = request.POST['title']
        post.content = request.POST['content']
        
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        
        post.save()
        
        return redirect('post_detail', post_id=post.id)
    return render(request, 'blog/update_post.html', {'post': post})

def delete_post(request, post_id):
    
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    return render(request, 'blog/delete_post.html', {'post': post})
