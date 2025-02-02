from django.shortcuts import render
from .models import Product

def product_list(request):
    # 公開済みのみの商品を取得
    products = Product.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'shop/product_list.html', {'products': products})
