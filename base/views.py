from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

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


@login_required(login_url='login')
def edit_post(request, pk):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    post = Post.objects.get(id=pk)

    if request.user != post.host:
        return HttpResponse("Not allowed here!")

    form = PostForm(instance=post)

    context = {'form': form}

    return render(request, 'base/post_form.html', context)


@login_required(login_url='login')
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'base/post_form.html', context)


def register_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)

            return redirect('home')

    page = 'register'

    context = {'page': page, 'form': form}

    return render(request, 'base/login_register.html', context)


def login_page(request):
    page = 'login'

    context = {'page': page}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'base/login_register.html', context)


def logout_page(request):
    logout(request)
    return redirect('home')
