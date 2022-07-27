from flask import Flask, render_template, request
from chat import getAnswer
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
    print(userText)
    return getAnswer(userText)

if __name__ == "__main__":
    app.run(port=8000, debug=True)