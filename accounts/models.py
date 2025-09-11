from django.db import models
from django.contrib.auth.models import AbstractUser # djangoが提供する一般的なユーザーモデル。そのまま使ってもいいし継承しても良い

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # メールアドレスを一意にするためにunique=Trueを設定