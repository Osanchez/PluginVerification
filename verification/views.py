from . models import Authentication
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .verify import Verification

# Create your views here.

# TODO: take passkey in the url, or come up with a better solution for verification


def verification(request, uuid4):
    print(uuid4)

    model = Authentication

    passphrase = 'test'
    passphrase_authenticate = 'test1'  # this is what the user will enter to authenticate

    generated_key = Verification.hash_id(passphrase)
    degenerated_key = Verification.check_id(generated_key, passphrase_authenticate)

    if model.objects.filter(authentic_key=uuid4).exists():
        retrieved = model.objects.get(authentic_key=uuid4)

        data = {
            'plugin_name': retrieved.plugin_name,
            'owner': retrieved.owner,
            'entered_phrase': passphrase,
            'generated_hashkey': generated_key,
            'is_authentic': degenerated_key,
        }

    else:
        data = {
            'plugin_name': 'N/A',
            'owner': 'N/A',
            'entered_phrase': passphrase,
            'generated_hashkey': generated_key,
            'is_authentic': degenerated_key,
        }

    return JsonResponse(data)

