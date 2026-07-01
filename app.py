from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!\nWelcome to Flask!", 200
    return "Hello World!" "yo", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
