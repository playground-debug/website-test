from django.shortcuts import render
from django.http import JsonResponse


def homepage(request):
    data = {
        'name': 'Ava',
        'age': '21',
    }
    return JsonResponse(data)


def home(request):
    return render(request, 'home/index.html')
