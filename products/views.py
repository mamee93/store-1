from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product
# Create your views here.
def product_list(request):
    product = Product.objects.all()
    return render(request,'product/product_list.html',{'product':product})

def product_details(request,id):
    product_desc = get_object_or_404(Product,id=id)
    return render(request,'product/singl_product.html',{'product_desc':product_desc})