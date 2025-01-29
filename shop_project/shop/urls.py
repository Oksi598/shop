from django.urls import path
from .views import index, product_detail, category_detail, add_product, edit_product, delete_product, register

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
    path('product/add/', add_product, name='add_product'),
    path('product/edit/<int:pk>/', edit_product, name='edit_product'),
    path('product/delete/<int:pk>/', delete_product, name='delete_product'),
    path('register/', register, name='register'),
]
