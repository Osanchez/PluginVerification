from . models import Authentication
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .verify import Verification

# Create your views here.


def verification(request, uuid4):
    print(uuid4)

    model = Authentication
    generated_key = Verification.hash_id('test')
    degenerated_key = Verification.check_id(generated_key, 'test')

    if model.objects.filter(authentic_key=uuid4).exists():
        retrieved = model.objects.get(authentic_key=uuid4)

        data = {
            'plugin_name': retrieved.plugin_name,
            'owner': retrieved.owner,
            'is_authentic': '',  # call verification tools
            'returned_key': uuid4,
            'hash_test_phrase': 'test',
            'generated_hashkey': generated_key,
            'degenerated_hashkey_matches': degenerated_key
        }

    else:
        data = {
            'plugin_name': 'N/A',
            'owner': 'N/A',
            'is_authentic': 'False',  # call verification tools
            'returned_key': uuid4,
            'hash_test_phrase': 'test',
            'generated_hashkey': generated_key,
            'degenerated_hashkey_matches': degenerated_key
        }

    return JsonResponse(data)

