from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'Store/home.html')


def about(request):
    return render(request, 'Store/about.html')