from django.urls import path
from .views import (products_list,
                    product_detail,
                    cart,
                    delete_cart_item,
                    edit_cart_item,
                    create_order,
                    orders,
                    rate_product)

urlpatterns = [
    path('', products_list, name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('delete/<int:pk>/item/', delete_cart_item, name='delete_item'),
    path('edit_cart_item/<int:pk>/', edit_cart_item, name='edit_cart_item'),
    path('cart/create_order/', create_order, name='create_order'),
    path('orders/', orders, name='orders'),
    path('rate/<int:pk>/product/', rate_product, name='rate_product'),
]
