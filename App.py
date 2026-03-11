from flask import Flask, request
import wikipedia

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>AI Study Bot</h2>
    <form action="/ask">
        <input name="q" placeholder="Ask a question">
        <button type="submit">Ask</button>
    </form>
    """

@app.route("/ask")
def ask():
    q = request.args.get("q")
    try:
        ans = wikipedia.summary(q, sentences=2)
    except:
        ans = "Sorry, I couldn't find the answer."
    return f"<h3>Answer:</h3><p>{ans}</p><br><a href='/'>Ask again</a>"

app.run(host="0.0.0.0", port=10000)
