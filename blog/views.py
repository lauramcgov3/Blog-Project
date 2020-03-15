from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def home(request):
    return render(request, 'blog/home.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


def post_edit(request, pk):
    obj = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(instance=obj, data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=obj)

    return render(request, 'blog/post_edit.html', {'form': form})


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()

    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
