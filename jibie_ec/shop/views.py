from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_list(request):
    # 公開済みのみの商品を取得
    products = Product.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id) #商品IDで情報取得し、商品が存在しない場合は404エラーを返す
    return render(request, 'shop/product_detail.html', {'product': product})

def cart_detail(request):
    # セッションからカートを取得
    cart = request.session.get('cart', {})
    # 商品データを取得
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []

    for product in products:
        cart_items.append({
            'product': product,
            'quantity': cart[str(product.id)],
            'total_price': product.price * cart[str(product.id)]
        })
    
    # 合計金額
    total_amount = sum(item['total_price'] for item in cart_items)

    return render(request, 'shop/cart_detail.html', {
        'cart_items': cart_items,
        'total_amount': total_amount
    })


def add_to_cart(request, product_id):
    #セッションからカートを取得し、なければからの辞書を入れる
    cart = request.session.get('cart', {}) 

    # すでに商品がある場合は数量を増やす
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    # ない場合は新しく追加
    else:
        cart[str(product_id)] = 1
    
    # カートをセッションに保存
    request.session['cart'] = cart
    # カート詳細ページへリダイレクト
    return redirect('cart_detail')