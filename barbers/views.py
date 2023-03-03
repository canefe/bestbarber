from django.shortcuts import render

def index(request):
    response = render(request, 'barbers/index.html')
    return response

def barbers(request):
    response = render(request, 'barbers/barbers.html')
    return response