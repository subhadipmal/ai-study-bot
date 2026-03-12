from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Study Bot</title>

<style>
body{font-family:Arial;background:#f2f2f2;margin:0;}
.header{background:#4CAF50;color:white;padding:15px;text-align:center;font-size:20px;}
.chatbox{padding:10px;height:70vh;overflow-y:auto;}
.msg{background:white;padding:10px;border-radius:8px;margin:5px;max-width:80%;}
.user{background:#DCF8C6;margin-left:auto;}
.inputbar{position:fixed;bottom:0;width:100%;display:flex;background:white;}
input{flex:1;padding:12px;border:none;outline:none;}
button{background:#4CAF50;color:white;border:none;padding:12px 20px;}
</style>

</head>
<body>

<div class="header">📚 AI Study Bot</div>

<div id="chat" class="chatbox"></div>

<div class="inputbar">
<input id="msg" placeholder="Ask study question...">
<button onclick="send()">Send</button>
</div>

<script>
function send(){
let msg=document.getElementById("msg").value;
if(msg=="") return;

let chat=document.getElementById("chat");
chat.innerHTML+=`<div class='msg user'>${msg}</div>`;
chat.innerHTML+=`<div class='msg'>Thinking...</div>`;

document.getElementById("msg").value="";
chat.scrollTop=chat.scrollHeight;
}
</script>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return html
