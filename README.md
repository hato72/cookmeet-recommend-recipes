# Cook Meet(レシピレコメンド処理)
![cookmeet](https://github.com/5skip/recommend-recipes/assets/139259020/0d435066-a6c4-4e08-b1fa-be5ddec7f440)

## 技術構成図
![技術構成図](https://github.com/5skip/recommend-recipes/assets/139259020/d6452c6d-9300-43b5-a53f-2bc9fe80f413)

## 使用した主なフレームワーク、ライブラリ
- [FastAPI](https://fastapi.tiangolo.com/ja/)・・・APIを構築するのに使用
- [LangChain](https://python.langchain.com/v0.1/docs/get_started/introduction/)・・・Geminiのプロンプト作成および返答結果の解析処理に使用

## デプロイ
Cloud Run (現在停止中)

## フロントエンド
ソースコード: https://github.com/hato72/CookMeet

デプロイ先：https://cook-meet.vercel.app/

## バックエンド(認証、作った料理の履歴)
ソースコード: https://github.com/hato72/go_backend_hackathon

デプロイ先: https://cookmeet-backend.onrender.com

## 実行方法
1. ルートディレクトリ直下に.envファイルを作成
2. [Rakuten Developers](https://webservice.rakuten.co.jp/)の「+New App」からアクセスキーを取得
3. [Google AI Studio](https://aistudio.google.com/app/prompts/new_chat?hl=ja)からGeminiのAPIキーを取得
4. `.env`ファイルに以下を記述
```
RAKUTEN_APPLICATION_ID=<取得したアクセスキー>
GOOGLE_API_KEY=<取得したAPIキー>
```
5. 【Vscodeの場合】拡張機能から「Dev Containers」をインストールし、コマンドパレットから`Open Folder in Container`を選択

6. 【Vscode以外】以下を実行
```
docker-compose build
docker-compose up -d
```





