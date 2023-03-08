from django.shortcuts import render

def index(request):
    response = render(request, 'barbers/index.html')
    return response
