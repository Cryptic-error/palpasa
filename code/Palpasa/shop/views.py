from django.shortcuts import redirect, render
from .models import Product, CartItem
from django.http import HttpResponse
from math import ceil



# def index(request):
#     Products =Product.objects.all()
#     print(Products)
#     n=len(Products)
#     nslides=n//4 + ceil((n/4)-(n//4))
#     params={'no of slides':nslides, 'range':range(nslides),'product': Products}
#     return render(request,"shop/index.html")

def index(request):
    Products = Product.objects.all()
    n = len(Products)
    print(Products)
    nslides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nslides, 'range': range(nslides), 'products': Products}
    return render(request, "shop/index.html", params)
# Create your views here.

def home(request):
    return render(request, "shop/homeage.html")

# views.py

from django.http import JsonResponse
from django.shortcuts import render
# from .models import Product  # Make sure to import your Product model
from math import ceil



def check(request):
    allprods = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nslides), nslides]) 

    params = {'allprods': allprods}
    return render(request, "shop/check.html", params)

def get_product_info(product_id):
    try:
        product = Product.objects.get(id=product_id)
        return {'name': product.name, 'price': product.price}  # Assuming 'name' and 'price' are fields in your Product model
    except Product.DoesNotExist:
        return None

def cart_view(request):
    cart = {'1': 2, '2': 1}  # Example cart object with product IDs and quantities
    cart_items = []

    for product_id, quantity in cart.items():
        product_info = get_product_info(product_id)
        if product_info:
            cart_items.append({
                'id': product_id,
                'name': product_info['name'],
                'price': product_info['price'],
                'quantity': quantity
            })

    return render(request, 'check.html', {'cart_items': cart_items})



    # Redirect back to the same page after adding the item to the cart
    return redirect('check')


def service(request):
    # Products = Product.objects.all()
    # n = len(Products)
    # nslides = n // 4 + ceil((n / 4) - (n // 4))

    allprods = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nslides), nslides]) 

    params = {'allprods': allprods}
    return render(request, "shop/service.html", params)
    


def about(request):
    return render(request, "shop/about.html")
def index2(request):
    return render(request, "shop/index2.html")
def portfolio(request):
    return render(request, "shop/portfolio.html")
def contact(request):
    return render(request, "shop/contact.html")
# def home(request):
#     return render(request, "shop\template\index.html")

