from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)


@app.route("/hello/<a>", methods=['GET'])
def hello(a):
    l = []
    a = 5
    a = int(a + 1)
    for i in range(1, a):
        abc = random.randint(1, 10)
        l.append(abc)
    return f'Wynik: {l}'


if __name__ == "__main__":
    app.run(debug=True)
