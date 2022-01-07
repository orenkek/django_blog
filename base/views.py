from django.http import HttpResponse
from django.shortcuts import render
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