# -*- coding: utf-8 -*-
"""
Gerador de senha -- mesma logica do script original (caracteres ASCII 33-125,
o mesmo intervalo de before), so trocando random.randint (nao seguro para
senhas) por secrets.choice (gerador criptografico do Python).
"""
import os
import secrets

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# chr(33) ate chr(125) inclusive -- mesmo conjunto do script original
CHARSET = [chr(c) for c in range(33, 126)]

MIN_LENGTH = 4
MAX_LENGTH = 256
DEFAULT_LENGTH = 16


def generate_password(length):
    return "".join(secrets.choice(CHARSET) for _ in range(length))


@app.route("/")
def index():
    return render_template(
        "index.html", min_length=MIN_LENGTH, max_length=MAX_LENGTH, default_length=DEFAULT_LENGTH
    )


@app.route("/generate")
def generate():
    try:
        length = int(request.args.get("length", DEFAULT_LENGTH))
    except (TypeError, ValueError):
        return jsonify({"error": "comprimento invalido"}), 400

    if not (MIN_LENGTH <= length <= MAX_LENGTH):
        return jsonify({"error": f"comprimento precisa estar entre {MIN_LENGTH} e {MAX_LENGTH}"}), 400

    return jsonify({"password": generate_password(length), "length": length})


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(debug=debug, host="0.0.0.0", port=int(os.environ.get("PORT", 5100)))
