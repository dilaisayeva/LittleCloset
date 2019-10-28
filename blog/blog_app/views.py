from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def product_add(request):
    return render(request,'product_add.html')
