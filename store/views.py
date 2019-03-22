from django.shortcuts import render
from .models import Plugin

# Create your views here.


def home(request):
    context = {
        'plugins': Plugin.objects.all(),
        'latest_plugin': Plugin.objects.first()
    }

    return render(request, 'Store/home.html', context)


def about(request):
    context = {
        'latest_plugin': Plugin.objects.first()
    }

    return render(request, 'Store/about.html', context)


def store(request):
    context = {
        'plugins': Plugin.objects.all(),
        'latest_plugin': Plugin.objects.first()
    }

    return render(request, 'Store/store.html', context)
