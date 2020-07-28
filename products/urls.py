from django.urls import path
from .views import product_list,product_details,product_add,product_edit
urlpatterns = [
    path('product', product_list, name='product_list'),
    path('product/add', product_add, name='product_add'),
    path('product/<int:id>', product_details, name='product_details'),
    path('product/<int:id>/edit', product_edit, name='product_edit'),
    
    
    
    
   
]
