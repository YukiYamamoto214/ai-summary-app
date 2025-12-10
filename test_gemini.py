import google.generativeai as genai

# APIキーを設定
api_key = "AIzaSyBbP95CHmejnrcDHwUYiMMFjhIN5QzAGXo"

genai.configure(api_key=api_key)

# モデルを設定
model = genai.GenerativeModel('gemini-flash-latest')

# テスト：簡単な要約をお願いする
test_text = """
人工知能（AI）は、コンピューターに人間のような知能を持たせる技術です。
最近では、ChatGPTやGeminiなどの生成AIが登場し、
文章の作成、翻訳、要約など様々なタスクができるようになりました。
企業での活用も進んでおり、業務効率化に貢献しています。
"""

print("=== Gemini API テスト ===")
print("元の文章:", test_text)
print("\n要約を生成中...\n")

response = model.generate_content(f"以下の文章を1-2文で要約してください：\n{test_text}")

print("=== 要約結果 ===")
print(response.text)
