from django.shortcuts import render
from django.db.models import Q
from .models import Product

def product_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    filters = Q()

    if query:
        filters &= Q(name__icontains=query) | Q(description__icontains=query)

    if category:
        filters &= Q(category__iexact=category)

    if min_price:
        filters &= Q(price__gte=min_price)

    if max_price:
        filters &= Q(price__lte=max_price)

    products = Product.objects.filter(filters)

    return render(request, 'products/product_list.html', {'products': products})
