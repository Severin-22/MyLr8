from django.shortcuts import render
from .models import Product, Client, Sale

def product_list(request):
    products = Product.objects.all()
    clients = Client.objects.all()
    sales = Sale.objects.all()
    return render(request, 'product_list.html', {
        'products': products,
        'clients': clients,
        'sales': sales
    })
