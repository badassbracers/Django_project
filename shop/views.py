from django.shortcuts import render
from .models import Category, Product


def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def proverka_shablona1(request):
    return render(request, 'shop/1.html')

def proverka_shablona2(request):
    return render(request, 'shop/2.html')
