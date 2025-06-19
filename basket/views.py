from django.shortcuts import render, get_object_or_404, redirect
from .basket import Basket
from shop.models import *
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import *
def basket_detail(request):
    basket = Basket(request)
    print("🧺 Содержимое корзины:", basket.basket)
    return render(request, 'basket/basket_detail.html', context={'basket': basket})

def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Products, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')

def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')

@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Products, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(
            product = product,
            count=form.cleaned_data['count'],
            update_count = form.cleaned_data['reload']
        )
    return redirect('basket_detail')

# @permision_required('shop.add_pos_order') для проверки прав доступа в [перчисляю несколько прав]

@login_required
def basket_buy(request):
    basket = Basket(request)
    if basket.__len__() <= 0:
        return redirect('basket_detail')
    form = OrderForm(request.POST)
    if form.is_valid():
        order = Bill.objects.create(
            clientName =form.cleaned_data['clientName'],
            clientSurname=form.cleaned_data['clientSurname'],
            clientMiddleName=form.cleaned_data['clientMiddleName'],
            comment=form.cleaned_data['comment'],
            delivery_address=form.cleaned_data['delivery_address'],
            delivery_type=form.cleaned_data['delivery_type'],
            total_price=basket.get_total_price()
        )
        for item in basket:
            pos_order = Pos_order.objects.create(
                product = item['product'],
                count = item['count'],
                bill = order
            )
        basket.clear()
    return redirect('basket_detail')

@login_required
def open_order(request):
    return render(request, 'order/order_form.html', context={'form_order':OrderForm})

def basket_increase(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    basket = Basket(request)
    basket.increase(product)
    return redirect('basket_detail')

def basket_decrease(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    basket = Basket(request)
    basket.decrease(product)
    return redirect('basket_detail')