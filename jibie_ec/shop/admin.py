from django.contrib import admin
from .models import Product

# これを書くことで、管理画面で商品管理ができるようになる
admin.site.register(Product)
