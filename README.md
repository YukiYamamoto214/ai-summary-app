# 🤖 AI文書要約くん

Google Gemini APIを使用した文書要約Webアプリケーション

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Gemini API](https://img.shields.io/badge/Gemini-API-orange)

## 📝 概要

テキストを入力すると、AIが自動で要約を生成するWebアプリケーションです。

### 使用技術

- **バックエンド**: Python, Flask
- **AI API**: Google Gemini API
- **フロントエンド**: HTML, CSS

## 🚀 セットアップ

### 1. リポジトリをクローン

```bash
git clone https://github.com/yourusername/ai-summary-app.git
cd ai-summary-app
```

### 2. 依存関係をインストール

```bash
pip install flask google-generativeai python-dotenv
```

### 3. 環境変数を設定

`.env` ファイルを作成し、Gemini APIキーを設定：

```
GEMINI_API_KEY=your_api_key_here
```

### 4. アプリを起動

```bash
python app.py
```

ブラウザで http://127.0.0.1:5000 にアクセス

## 📸 スクリーンショット

アプリの画面イメージ（後で追加予定）

## 🛠️ 機能

- テキスト入力による文書要約
- リアルタイムAI処理
- レスポンシブデザイン

## 📄 ライセンス

MIT License
