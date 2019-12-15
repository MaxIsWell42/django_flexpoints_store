from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Mock data
products = [
    {
        'title': 'One Flex point',
        'cost': '$1',
        'image': '/static/contractor/flex.jpg',
        'likes': '0'
    },
    {
        'title': 'Five Flex points',
        'cost': '$5',
        'image': '/static/contractor/flex.jpg',
    },
    {
        'title': '10 Flex points',
        'cost': '$9',
        'image': '/static/contractor/flex.jpg',
    }   
]

def home(request):
    context = {
        'products': products
        # 'products': Product.objects.all()
    }
    return render(request, 'contractor/home.html', context)

def about(request):
    return render(request, 'contractor/about.html')