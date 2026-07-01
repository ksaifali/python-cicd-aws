from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!\nWelcome to Flask!", 200
<<<<<<< Updated upstream
    return "Hello World!" "yo-yo-honey", 200
=======
    return "Hello World!" "yo-yo-honey-singh-yo", 200
>>>>>>> Stashed changes

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
test minor bump v2 # or make any real small change
