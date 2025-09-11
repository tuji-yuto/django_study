# Django学習 - 進捗管理

## 📅 最終更新日：2025/09/12

## ✅ 完了済み項目

### CustomUserモデル
- [x] AbstractUserを継承したCustomUserクラス作成
- [x] `email = models.EmailField(unique=True)`でメール重複防止設定
- [x] settings.pyに`AUTH_USER_MODEL = 'accounts.CustomUser'`設定
- [x] マイグレーション作成・適用済み
- [x] 管理画面(admin.py)に登録済み
- [x] スーパーユーザー作成済み（username: master123）

### テンプレート設定
- [x] templates/login.html作成
- [x] settings.pyの`DIRS: [BASE_DIR / 'templates']`設定
- [x] HTMLフォームをAjax用からHTTP用に書き換え完了
  - method="POST", action="/accounts/process/"
  - name属性設定（id属性からname属性に変更）
  - {% csrf_token %}追加

### View関数
- [x] login_page関数：ログイン画面表示用
- [x] login_process関数：認証処理用
  - authenticate()による実際のDB認証
  - login()によるセッション管理
  - 成功時：redirect()でページ移動
  - 失敗時：render()でエラーメッセージ表示

### URL設定
- [x] accounts/urls.py設定完了
  - path('', views.login_page, name='login_page')
  - path('process/', views.login_process, name='login_process')

## 🎯 次回やること（優先度順）

### 1. 実際のログイン機能テスト
- [ ] 開発サーバー起動：`python manage.py runserver`
- [ ] http://127.0.0.1:8000/accounts/ にアクセス
- [ ] 作成済みスーパーユーザーでログインテスト
- [ ] ログイン成功・失敗パターンの動作確認

### 2. エラーハンドリング改善
- [ ] login.htmlでのエラーメッセージ表示確認
- [ ] 不正なリクエスト時の動作確認

### 3. Ajax版実装（学習用）
- [ ] 現在のHTTP版をAjax版に書き換え
- [ ] JavaScript（fetch API）実装
- [ ] JSONレスポンス対応

## 📚 重要な学習ポイント（復習用）

### CSRF攻撃と対策
- **攻撃シナリオ**：悪意のあるサイトから勝手に操作される
- **対策**：CSRFトークンによる正当性確認
- **技術的根拠**：同一オリジンポリシーで攻撃者がトークン取得不可

### Django認証システム
- **authenticate()**：実際のDB照合（成功→Userオブジェクト、失敗→None）
- **login()**：セッション管理
- **redirect() vs render()**：ページ移動 vs HTML直接送信

### URL設計
- **name属性**：Django特有のURL逆引きシステム
- **redirect('login_page')**：urls.pyのname検索（import不要）

## 🗂️ 現在のファイル構造

```
django_study/
├── manage.py
├── db.sqlite3
├── CLAUDE.md（学習方針）
├── PROGRESS.md（このファイル）
├── templates/
│   └── login.html
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── accounts/
│   ├── __init__.py
│   ├── admin.py（CustomUser登録済み）
│   ├── apps.py
│   ├── models.py（CustomUser定義済み）
│   ├── views.py（login_page, login_process実装済み）
│   ├── urls.py（URL設定済み）
│   ├── tests.py
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
└── venv/（仮想環境）
```

## 💡 次回学習開始時のチェックリスト

1. [ ] `python manage.py runserver`でサーバー起動
2. [ ] http://127.0.0.1:8000/accounts/ でログインページ表示確認
3. [ ] master123 / 設定パスワードでログインテスト
4. [ ] 間違ったパスワードでエラー表示確認

## ⚠️ 注意点

- **master123ユーザー**：バイパスしたパスワード（短い・簡単）を使用
- **CSRF設定**：DEBUG=Trueのため開発環境でのみ動作
- **セキュリティ**：本番環境用の設定は未実装