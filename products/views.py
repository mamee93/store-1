from django.shortcuts import render
from django.utils import timezone
from .models import Product
# Create your views here.
def product_list(request):
    product = Product.objects.all()
    return render(request,'product_list.html',{'product':product})

def product(request,id):
    product_desc = Product.objects.get(id=id)
    return render(request,'singl_product.html',{'product_desc':product_desc})