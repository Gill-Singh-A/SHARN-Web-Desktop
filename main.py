#! /usr/bin/env python3

from flask import Flask, render_template, request

app = Flask(__name__)
host = "127.0.0.1"
port = 7020

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)