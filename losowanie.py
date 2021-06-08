from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)


@app.route("/hello/<abc>", methods=['GET'])
def hello(abc):
    l = []
    if abc in [l]:
        l.pop()
    else:
        for i in range(1, 7):
            abc = random.randint(1, 49)
            l.append(abc)
    return f'Wynik: {l}'



if __name__ == "__main__":
    app.run(debug=True)
