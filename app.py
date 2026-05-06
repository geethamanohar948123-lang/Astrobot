import os
from flask import Flask, render_template, request, jsonify, redirect, url_for
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from file.env
load_dotenv("file.env")

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback-secret-key")  # Required for redirect/session logic

# Initialize Groq Client with the GROQ_API_KEY env var
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chat.html')

@app.route('/login', methods=['POST'])
def handle_login():
    # Add simple validation here if needed
    return redirect(url_for('chatbot'))

@app.route('/send', methods=['POST'])
def send():
    try:
        user_data = request.get_json()
        user_message = user_data.get('message')

        if not user_message:
            return jsonify({"reply": "Message is empty!"}), 400

        # Groq API Call using the SDK
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """You are a helpful AI assistant.

Rules:
1. Always give correct and practical answers.
2. Present answers in clear step-by-step format.
3. Use numbered steps (Step 1, Step 2, etc.).
4. Keep explanations simple and easy to understand."""
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,  # Adds a bit of creativity
            max_tokens=1024,
        )

        reply = chat_completion.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "Sorry, I'm having trouble thinking backwards right now."}), 500

if __name__ == "__main__":
    app.run(debug=True)