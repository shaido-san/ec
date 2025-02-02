import os
import uuid
from django.db import models


# ファイルアップロード用の関数
def upload_image(instance, filename):
    # UUIDを使用して保存する。unique_id変数に生成した一意のUUIDを保存する
    unique_id = str(uuid.uuid4())
    return f"products/{unique_id}/{filename}"

class Product(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    information = models.TextField(blank=True)
    sold_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default="", blank=True, upload_to=upload_image)

    def __str__(self):
        return self.name
