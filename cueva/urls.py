 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
   
    path('product_create/', views.product_create, name='product_create'),
    path('category_list/', views.category_list, name='category_list'),
    path('products_by_category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    
]
