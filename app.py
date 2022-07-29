from flask import Flask, render_template, request
from tf_train import chat
app = Flask(__name__)


    

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/resources")
def resources():
    return render_template("page2.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chat(userText)

