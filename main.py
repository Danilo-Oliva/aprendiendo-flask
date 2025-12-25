from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstap = Bootstrap(app)


items = ["Arroz", "Huevos", "Café", "Leche"]

@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html', error = error)


@app.route("/index")
def index():
    user_ip_information = request.remote_addr

    # La persona que entre al index va a ser automaticamente dirigido hacia la ruta que le digamos al redirect
    response = make_response(redirect("/show_information_address"))
    # con esta response voy a crear una cookie
    response.set_cookie("user_ip_information", user_ip_information)

    return response


@app.route("/show_information_address")
def show_information():
    user_ip = request.cookies.get("user_ip_information")
    # creo el diccionario que contendrá todos los parametros del render_template
    context = {"user_ip": user_ip, "items": items}

    return render_template("ip_information.html", **context)


app.run(host="0.0.0.0", port=81, debug=True)
