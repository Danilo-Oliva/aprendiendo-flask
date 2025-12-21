from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    user_information = request.remote_addr
    return f"Hola como estas, tu dirección IP es la siguiente: {user_information}"


app.run(host="0.0.0.0", port=81, debug=True)