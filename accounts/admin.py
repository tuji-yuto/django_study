from django.contrib import admin
from .models import CustomUser

# Register your models here.

admin.site.register(CustomUser)  # カスタムユーザーモデルを管理サイトに登録　　admin ←モジュール　site ←クラス　register ←メソッド
