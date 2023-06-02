from django.http import JsonResponse
from django.shortcuts import render


def demo_api(request):
    return JsonResponse({
        'data': 'hello world'
    },
        safe=False
    )
