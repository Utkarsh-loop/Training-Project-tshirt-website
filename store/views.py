from django.shortcuts import render
from .models import Product

def home(request):
    featured_products = Product.objects.all()[:3]
    return render(request, 'store/home.html', {'products': featured_products})

def about(request):
    return render(request, 'store/about.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'store/shop.html', {'products': products})

def contact(request):
    if request.method == 'POST':
        # Just simple logging for demo purposes
        print("Received contact form submission:", request.POST)
        from django.contrib import messages
        messages.success(request, "Thanks for reaching out! We will get back to you shortly.")
    return render(request, 'store/contact.html')
