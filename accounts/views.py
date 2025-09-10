from django.http import JsonResponse #javaScriptで受け取れるようにする(JSON形式)
import json # json形式を扱うための様々な関数が入っている

# Create your views here.

def login_view(request):# request : ユーザーから送られてくる情報が入っている
    if request.method == 'POST': # .methodにはget or postが入っている
        # ここにあとでID・パスワードのチェック処理を書く
        return JsonResponse({'status': 'success', 'message': 'ログイン成功！'})# 第一引数に辞書型でデータを入れる。
    else:
        return JsonResponse({'status': 'error', 'message': '無効なリクエストです。'}, status=400)# statusはHTTPステータスコードを指定できる。デフォルトは200(成功)
