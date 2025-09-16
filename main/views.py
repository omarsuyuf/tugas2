# main/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers

from .models import Product
from .forms import ProductForm


def show_main(request):
    product_list = Product.objects.all()

    context = {
        "npm": "2406421200",
        "name": "Omar Suyuf Wicaksono",
        "class": "PBP E",
        "product_list": product_list,
        "app_name": "Football Shop",
    }
    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")

    context = {"form": form}
    return render(request, "create_product.html", context)


def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {"product": product}
    return render(request, "product_detail.html", context)


def show_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")


def show_xml_by_id(request, id):
    try:
        product = Product.objects.get(pk=id)  
        xml_data = serializers.serialize("xml", [product])  
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        product = Product.objects.get(pk=id)
        json_data = serializers.serialize("json", [product]) 
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)