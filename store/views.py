from django.shortcuts import render
from .models import Plugin, Post

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all(),
        'latest_plugin': Plugin.objects.first(),
        'latest_post': Post.objects.first()
    }

    return render(request, 'Store/home.html', context)


def about(request):
    context = {
        'latest_plugin': Plugin.objects.first(),
        'latest_post': Post.objects.first()
    }

    return render(request, 'Store/about.html', context)


def store(request):
    context = {
        'plugins': Plugin.objects.all(),
        'latest_plugin': Plugin.objects.first(),
        'latest_post': Post.objects.first()
    }

    return render(request, 'Store/store.html', context)
