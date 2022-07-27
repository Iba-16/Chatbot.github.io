from flask import Flask, render_template, request


app = Flask(__name__)


    

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(my_bot.get_response(userText))

if __name__ == "__main__":
    app.run(port=8000, debug=True)