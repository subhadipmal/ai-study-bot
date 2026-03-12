from fastapi import FastAPI
import wikipedia

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Study Bot running successfully"}

@app.get("/ask")
def ask(question: str):
    try:
        answer = wikipedia.summary(question, sentences=2)
        return {"question": question, "answer": answer}
    except:
        return {"answer": "Sorry, I couldn't find the answer."}
