# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello Word</h1>"


if __name__ == "__main__":
    app.run()
