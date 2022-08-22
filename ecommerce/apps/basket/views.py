from django.shortcuts import render, get_object_or_404
from .basket import Basket
from ecommerce.apps.catalogue.models import Product
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.

def basket_summary(request):
    basket = Basket(request)
    return render(request, 'basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    json_request = json.loads(request.body)
    if json_request['action'] == 'post':
        product_id = int(json_request['product_id'])
        product_qty = int(json_request['product_qty'])
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({'qty': basket_qty})
        return response


def basket_delete(request):
    basket = Basket(request)
    json_request = json.loads(request.body)
    if json_request['action'] == 'post':
        product_id = int(json_request['product_id'])
        basket.delete(product=product_id)
        basket_total = basket.get_total_price()
        response = JsonResponse({'qty': len(basket), 'subtotal': basket_total})
        return response


def basket_update(request):
    basket = Basket(request)
    json_request = json.loads(request.body)
    if json_request['action'] == 'post':
        product_id = int(json_request['product_id'])
        product_qty = int(json_request['product_qty'])
        print(product_id, product_qty)
        basket.update(product=product_id, qty=product_qty)
        basketsubtotal = basket.get_subtotal_price()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': len(basket), 'subtotal': basketsubtotal, 'total': baskettotal})
        return response