from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import BlogPost
from .forms import BlogPostForm

def home(request):
    query = request.GET.get('q')
    if query:
        posts = BlogPost.objects.filter(title__icontains=query)
    else:
        posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            guest_user, _ = User.objects.get_or_create(username='Guest', defaults={'password': 'guest'})
            post.author = guest_user

            post.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})



def update_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    
    if post.author.username != 'Guest':
        return redirect('home')
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPostForm(instance=post)
    
    return render(request, 'blog/create_post.html', {'form': form})


def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if post.author.username == 'Guest':
        post.delete()
    return redirect('home')