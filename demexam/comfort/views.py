from django.shortcuts import render
from .models import Products
def product_list(request):
    products = Products.objects.all()
    return render(request, 'products/products_list.html', {'products': products})

def main_page(request):
    return render(request, 'products/main_page.html')
# Create your views here.
