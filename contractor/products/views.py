from django.shortcuts import render
from django.http import HttpResponse

# Mock data
products = [
    {
        'title': 'A single Flex point',
        'cost': '$1'
    },
    {
        'title': 'Five Flex points',
        'cost': '$5'
    },
    {
        'title': '10 Flex points',
        'cost': '$9'
    }   
]

def home(request):
    context = {
        'products': products
    }
    return render(request, 'contractor/home.html', context)

def about(request):
    return render(request, 'contractor/about.html')