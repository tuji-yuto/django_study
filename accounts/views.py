from django.http import JsonResponse #javaScriptで受け取れるようにする(JSON形式)
import json # json形式を扱うための様々な関数が入っている
from django.shortcuts import render # HTMLテンプレートを処理してHTTPレスポンスを返す関数
from django.contrib.auth import authenticate, login# ユーザー認証とログイン処理を行う関数
from django.shortcuts import redirect# HTTP形式でのページ移動

# Create your views here.

def login_page(request):
    return render(request, 'login.html') # login.htmlを表示する

def login_process(request):# request : ユーザーから送られてくる情報が入っている
    if request.method == 'POST': # .methodにはget or postが入っている
            username = request.POST.get('username') # .POSTは辞書型。get('キー')で値を取り出せる。
            password = request.POST.get('password')
            print(username, password) # 確認用。サーバーのコンソールに表示される。

            user = authenticate(username=username, password=password)# ユーザー認証を行う。成功するとuserオブジェクトが返る。失敗するとNoneが返る。

            if user is not None: # userがNoneじゃなかった場合
                 login(request, user) # ログイン処理を行う
                 print("ログイン成功") # 確認用。サーバーのコンソールに表示される。
                 return JsonResponse({"status": "success","message":"ログインに成功しました"})
            else:#失敗したとき
                 print("ログイン失敗") # 確認用。サーバーのコンソールに表示される。
                 return JsonResponse({"status": "error","message":"ログインに失敗しました"},status=400) # status=400は認証エラーを意味する
