from django.urls import path # path　＝　urlを指定するために使う関数
from . import views # . は今いるディレクトリを指す。urls.pyと同じ階層ってこと。つまりaccountsディレクトリ

# urlはurlpatternsというリストに入れていく。リスト名はDjangoで決まっている。
# myproject/accounts　にいる。　その後ろ部分を指定していく。
# ('urlのパス', 実行したいviewsの関数, このurlの名前)
urlpatterns = [   
   path('', views.home_view, name='home_view'),
   path('process/', views.login_process, name='login_process'),

]