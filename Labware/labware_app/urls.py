from django.urls import path,include
from labware_app import views
from random import randint
num=randint(0,3498)

urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    # path('products',views.products,name="products"),
    path('infrastructure',views.infrastructure,name="infrastructure"),
    path('products/', views.product_list, name='product_list'),
    path('product-{num}/<int:product_id>/', views.product_details, name='product_details'),

]
      