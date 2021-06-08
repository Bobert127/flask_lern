from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/hello/<a>+<b>", methods=['GET'])
def hello(a, b):
    #a = 5
    #b = 3
    sumliczb = int(a) + int(b)
    return f'Wynik: {sumliczb}'


if __name__ == "__main__":
    app.run(debug=True)