# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    return render(request, 'webapp/index.html')


def about(request):
    return render(request, 'webapp/about.html')


def product_detail_view(request, **kwargs):
    id = kwargs['id_value']
    item = Item.objects.get(id=id)
    context = {'item': item}
    return render(request, 'webapp/product_detail.html', context)


def product_view(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'webapp/product.html', context)


def quick_view(request, **kwargs):
    id = kwargs['id_value']
    items = Item.objects.all()
    item = Item.objects.get(id=id)
    context = {'item': item, 'items': items}
    return render(request, 'webapp/quick_view.html', context)


def add_cart(request, **kwargs):
    item_name = kwargs['item_name']
    items = Item.objects.all()
    item = Item.objects.get(title=item_name)
    context = {'item': item, 'items': items}
    return render(request, 'webapp/product.html', context)