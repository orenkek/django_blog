from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()

    context = {'posts': posts}

    return render(request, 'base/home.html', context)
