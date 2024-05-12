# Cook Meet(レシピレコメンド処理)
![cookmeet](https://private-user-images.githubusercontent.com/139688965/328872226-54235b01-2da0-491e-857c-18581b70b518.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTU0OTI1OTcsIm5iZiI6MTcxNTQ5MjI5NywicGF0aCI6Ii8xMzk2ODg5NjUvMzI4ODcyMjI2LTU0MjM1YjAxLTJkYTAtNDkxZS04NTdjLTE4NTgxYjcwYjUxOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNTEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDUxMlQwNTM4MTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01NTE4YmIyM2Y4ZTZjNDE1YjVmMGUzZDE1ZmQxMmIzYWFiNThjNTU0NThmNGU0ZTJkNTM0ZmE2YzIwM2RjODY4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9._MmHDM7I-lxzv7BYTASj2EBQ26ItsXtOc0PuCBqXQ10)

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





