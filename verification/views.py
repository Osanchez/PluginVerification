from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def verification(request):
    data = {
        'plugin_name': '',
        'owner': '',
        'is_authentic': '',
        'returned_key': ''
    }
    return JsonResponse(data)
