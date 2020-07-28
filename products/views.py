from django.shortcuts import render, get_object_or_404,redirect 
from django.utils import timezone
from .models import Product
from .forms import AddProductForm
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request,'product/products-list.html',{'products':products})

def product_details(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'product/product-details.html',{'product':product})

def product_add(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)

        if form.is_valid():
                form.save()
                return  redirect ('/')

    else:
        form = AddProductForm()

    return render(request,'product/product-add.html',{'form':form})

def product_edit(request,id):
    product = get_object_or_404(Product,id=id)
    if request.method == 'POST':
        form = AddProductForm(request.POST,request.FILES,instance=product)

        if form.is_valid():
                form.save()
                return  redirect ('/product-add-successful')

    else:
        form = AddProductForm(instance=product)

    return render(request,'product/product-add.html',{'form':form})

