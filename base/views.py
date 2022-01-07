from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post


# Create your views here.

def home(request):
    posts = Post.objects.all()

    context = {'posts': posts}

    return render(request, 'base/home.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)

    context = {'post': post}

    return render(request, 'base/post.html', context)


def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'base/post_form.html', context)