from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("<h1>This is home.</h1>")

def json(request):
    return JsonResponse({'name': 'shayan'})