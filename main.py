from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/bye")
def bye_world():
    return "Bye World!"



if __name__ == "__main__":
    app.run(debug=True)

