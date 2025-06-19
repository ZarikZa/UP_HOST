from django.urls import path, include
from .views import *

urlpatterns = [
    path('', basket_detail, name='basket_detail'),
    path('remove/<int:product_id>', basket_remove, name='basket_remove'),
    path('add/<int:product_id>', basket_add, name='basket_add'),
    path('increase/<int:product_id>', basket_increase, name='basket_increase'),
    path('decrease/<int:product_id>', basket_decrease, name='basket_decrease'),
    path('clear/', basket_clear, name='basket_clear'),
    path('buy/', basket_buy, name='basket_buy'),
    path('create_order/', open_order, name='open_order'),
]

