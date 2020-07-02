from django.urls import path
from .views import product_list,product
urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:id>', product, name='product_list'),
    
    
   
]
