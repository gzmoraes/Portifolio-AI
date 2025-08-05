from flask import Flask, request, jsonify
from flask_cors import CORS
from .ai import AIBot

App = Flask(__name__)
CORS(App)  # Enable CORS for all routes
Ai = AIBot()


# @App.route("/")
# def index():
#     return render_template("index.html")


@App.route("/prompt", methods=["POST"])
def prompt():
    data = request.get_json()  # Obtém os dados JSON da requisição
    user_input = data.get("input")  # Extrai o input da requisição
    dict_response = Ai.chat(user_input)

    # Retorna a resposta como JSON
    return jsonify(dict_response)
