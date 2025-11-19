from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from .models import Product
from .forms import ProductForm
import requests
import json

User = get_user_model()



@login_required(login_url='/login')
def show_main(request):
    print(f"show_main - User authenticated: {request.user.is_authenticated}")  # Debug
    print(f"show_main - Username: {request.user.username if request.user.is_authenticated else 'Anonymous'}")  # Debug
    
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        "npm": "2406421200",
        "name": "Omar Suyuf Wicaksono",
        "class": "PBP E",
        "product_list": product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        "app_name": "Football Shop",
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect("main:show_main")

    context = {"form": form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
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
    product_list = Product.objects.all().order_by("-created_at")
    data = [
        {
            "id": str(product.id),
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "category": product.category,
            "thumbnail": product.thumbnail,
            "product_views": product.product_views,
            "is_featured": product.is_featured,
            "created_at": product.created_at.isoformat() if product.created_at else None,
            "user_id": getattr(product, "user_id", None),
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, id):
    try:
        product = Product.objects.get(pk=id)  
        xml_data = serializers.serialize("xml", [product])  
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, id):
    try:
        product = Product.objects.select_related('user').get(pk=id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': getattr(product, 'user_id', None),
            'user_username': product.user.username if getattr(product, 'user_id', None) else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def _is_ajax(request):
    h = request.headers
    return h.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in (h.get('accept') or '')

def register(request): 
    if request.method == 'POST':
        username  = (request.POST.get('username') or '').strip()
        password1 = request.POST.get('password1') or ''
        password2 = request.POST.get('password2') or ''

        if not username or not password1 or not password2:
            msg = 'Lengkapi semua field.'
            if _is_ajax(request): return JsonResponse({'ok': False, 'error': msg}, status=400)
            messages.error(request, msg); return render(request, 'register.html', {})
        if password1 != password2:
            msg = 'Password tidak sama.'
            if _is_ajax(request): return JsonResponse({'ok': False, 'error': msg}, status=400)
            messages.error(request, msg); return render(request, 'register.html', {})
        if User.objects.filter(username=username).exists():
            msg = 'Username sudah dipakai.'
            if _is_ajax(request): return JsonResponse({'ok': False, 'error': msg}, status=400)
            messages.error(request, msg); return render(request, 'register.html', {})

        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        if _is_ajax(request):
            return JsonResponse({'ok': True}, status=201)
        messages.success(request, 'Registrasi sukses.')
        return redirect('main:show_main')

    return render(request, 'register.html', {})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if _is_ajax(request):
                response = JsonResponse({'ok': True}, status=200)
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            
            messages.success(request, 'Login sukses.')
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            # Form tidak valid
            if _is_ajax(request):
                return JsonResponse({'ok': False, 'error': 'Username atau password salah.'}, status=400)
            messages.error(request, 'Username atau password salah.')
    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = (request.POST.get("name") or "").strip()
    description = request.POST.get("description") or ""
    category = request.POST.get("category") or ""
    thumbnail = request.POST.get("thumbnail") or ""
    is_featured = (request.POST.get("is_featured") == "on")
    raw_price = request.POST.get("price") or "0"
    try:
        price = int(raw_price)
    except ValueError:
        price = 0
    user = getattr(request, "user", None)

    new_product = Product(
        name=name,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        price=price,
        user=user if user and user.is_authenticated else None,
    )
    new_product.save()
    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def update_product_entry_ajax(request, id): 
    try:
        product = Product.objects.select_related('user').get(pk=id)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

    name = (request.POST.get("name") or "").strip()
    description = request.POST.get("description") or ""
    category = request.POST.get("category") or ""
    thumbnail = request.POST.get("thumbnail") or ""
    is_featured = (request.POST.get("is_featured") == "on")

    raw_price = request.POST.get("price") or None
    if raw_price is not None:
        try:
            product.price = int(raw_price)
        except ValueError:
            pass  

    if name: product.name = name
    product.description = description
    product.category = category
    product.thumbnail = thumbnail
    product.is_featured = is_featured

    product.save()
    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
@require_POST
def delete_product_entry_ajax(request, id):
    try:
        product = Product.objects.get(pk=id)

        product.delete()
        return HttpResponse(b"DELETED", status=200)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))
        description = strip_tags(data.get("description", ""))
        price = data.get("price", 0)
        thumbnail = data.get("thumbnail", "")  # GANTI dari "image" ke "thumbnail"
        category = data.get("category", "")
        is_featured = data.get("is_featured", False)  # TAMBAH ini
        user = request.user
        
        new_product = Product(
            name=name, 
            description=description,
            price=price,
            thumbnail=thumbnail,  # GANTI dari image ke thumbnail
            category=category,
            is_featured=is_featured,  # TAMBAH ini
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)