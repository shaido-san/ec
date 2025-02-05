from . import views
from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('user/', views.user, name='user'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.product_list, name='product_list'), # 商品一覧ページ
    path('product/<int:product_id>/', views.product_detail, name='product_detail'), # 商品詳細ページ
    path('cart/', views.cart_detail, name='cart_detail'), #カートページ
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'), #カート詳細ページ
    path('checkout/', views.checkout, name='checkout'), #決済処理をするルート
    path('checkout/success/', views.checkout_success, name='checkout_success'), # 購入完了ページへ
]