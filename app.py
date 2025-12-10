from flask import Flask, render_template, request
import google.generativeai as genai
import os

# Flaskアプリ初期化
app = Flask(__name__)

# Gemini API設定（環境変数から読み込み）
api_key = os.environ.get('GEMINI_API_KEY')
if not api_key:
    # .envファイルから読み込み
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-flash-latest')

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    original_text = ""
    
    if request.method == 'POST':
        original_text = request.form.get('text', '')
        if original_text.strip():
            try:
                response = model.generate_content(
                    f"以下の文章を簡潔に要約してください：\n{original_text}"
                )
                summary = response.text
            except Exception as e:
                summary = f"エラーが発生しました: {str(e)}"
    
    return render_template('index.html', summary=summary, original_text=original_text)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
