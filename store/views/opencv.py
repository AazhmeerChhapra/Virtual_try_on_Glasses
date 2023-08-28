from django.shortcuts import render , redirect , HttpResponseRedirect, get_object_or_404
from store.models.product import Products
from store.models.category import Category
from django.views import View


def opencv(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    products = Products.get_all_products()
    data = {}
    data['product'] = product
    data['products'] = products
    return render(request, 'opencv.html', data)
