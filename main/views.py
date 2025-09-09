from django.shortcuts import render

def home(request):
    ctx = {"app_name": "Football Shop", "name": "Nama Kamu", "class": "Kelas Kamu"}
    return render(request, "home.html", ctx)
