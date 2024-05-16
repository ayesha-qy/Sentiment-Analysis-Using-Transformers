# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from model import analyze_sentiment

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    result = analyze_sentiment(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
