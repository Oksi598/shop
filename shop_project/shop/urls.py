from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.index, name="index"),
    path('product/<int:pk>/', views.product_detail, name="product_detail"),
    path('category/<int:pk>/', views.category_detail, name="category_detail"),
    path('product/add/', views.add_product, name="add_product"),
    path('product/edit/<int:pk>/', views.edit_product, name="edit_product"),
    path('product/delete/<int:pk>/', views.delete_product, name="delete_product"),
    path('register/', views.register, name="register"),
]
