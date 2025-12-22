from flask import Flask, request, make_response, redirect

app = Flask(__name__)


@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    
    #La persona que entre al index va a ser automaticamente dirigido hacia la ruta que le digamos al redirect
    response = make_response(redirect("/show_information_address"))
    #con esta response voy a crear una cookie
    response.set_cookie("user_ip_information", user_ip_information)
    
    return response
    
@app.route("/show_information_address")
def show_information():
    user_ip = request.cookies.get("user_ip_information")
    return f"Hola, tu dirección IP es: {user_ip}"

app.run(host="0.0.0.0", port=81, debug=True)