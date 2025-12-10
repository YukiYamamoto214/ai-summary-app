from flask import Flask, render_template, request
import google.generativeai as genai
import os

# Flaskアプリ初期化
app = Flask(__name__)

# Gemini API設定（環境変数から読み込み）
api_key = os.environ.get('GEMINI_API_KEY')
if not api_key:
    # ローカル開発用：.envファイルから読み込み
    try:
        from dotenv import load_dotenv
        load_dotenv()
        api_key = os.environ.get('GEMINI_API_KEY')
    except:
        pass

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-flash-latest')
else:
    model = None

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    original_text = ""
    
    if request.method == 'POST':
        original_text = request.form.get('text', '')
        if original_text.strip():
            if model:
                try:
                    response = model.generate_content(
                        f"以下の文章を簡潔に要約してください：\n{original_text}"
                    )
                    summary = response.text
                except Exception as e:
                    summary = f"エラーが発生しました: {str(e)}"
            else:
                summary = "APIキーが設定されていません"
    
    return render_template('index.html', summary=summary, original_text=original_text)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
