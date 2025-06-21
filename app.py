import os
from openai import OpenAI
from flask import Flask, request, jsonify

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    return jsonify(response.choices[0].message.content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)