from django.urls import path # path　＝　urlを指定するために使う関数
from . import views # . は今いるディレクトリを指す。urls.pyと同じ階層ってこと。つまりaccountsディレクトリ

# urlはurlpatternsというリストに入れていく。リスト名はDjangoで決まっている。
# myproject/accounts　にいる。　その後ろ部分を指定していく。
# ('urlのパス', 実行したいviewsの関数, このurlの名前)
urlpatterns = [   
   path('', views.login_page, name='login_page'),  # login/ にアクセスしたらviews.pyのlogin_page関数を実行する。''は空文字で、何も指定しないことを意味する。つまりaccounts/までアクセスしたらlogin_page関数を実行する。
   path('process/', views.login_process, name='login_process'),

]