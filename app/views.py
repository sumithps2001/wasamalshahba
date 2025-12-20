from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def singleproduct(request):
    return render(request, 'single-product.html')

def contact(request):
    return render(request, 'contact.html')