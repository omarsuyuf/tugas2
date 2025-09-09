from django.shortcuts import render
from .models import Product


def home(request):
    ctx = {"app_name": "Football Shop", 
           "name": "Omar Suyuf Wicaksono", 
           "class": "PBP E",
           "npm" : "2406421200",
           "products": Product.objects.all()}
    return render(request, "main.html", ctx)
