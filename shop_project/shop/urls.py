from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.index, name="index"),
    path('product/<int:pk>/', views.product_detail, name="product_detail"),
    path('category/<int:pk>/', views.category_detail, name="category_detail"),
    path('product/add/', views.add_product, name="add_product"),
    path('product/edit/<int:pk>/', views.edit_product, name="edit_product"),
    path('product/delete/<int:pk>/', views.delete_product, name="delete_product"),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout")
    ]
