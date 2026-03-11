from flask import Flask, request, jsonify
import wikipedia

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Study Bot is running"

@app.route("/ask")
def ask():
    q = request.args.get("q")
    try:
        ans = wikipedia.summary(q, sentences=2)
    except:
        ans = "Topic not found"
    return jsonify({"answer": ans})

app.run(host="0.0.0.0", port=10000)
