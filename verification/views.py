from . models import Authentication
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.


def verification(request, uuid4):
    print(uuid4)

    model = Authentication

    if model.objects.filter(authentic_key=uuid4).exists():
        retrieved = model.objects.get(authentic_key=uuid4)

        data = {
            'plugin_name': retrieved.plugin_name,
            'owner': retrieved.owner,
            'is_authentic': '',  # call verification tools
            'returned_key': uuid4
        }

    else:
        data = {
            'plugin_name': 'N/A',
            'owner': 'N/A',
            'is_authentic': 'False',  # call verification tools
            'returned_key': uuid4
        }

    return JsonResponse(data)

