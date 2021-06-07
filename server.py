from flask import Flask

app = Flask(__name__)


@app.route("/hello/")
def hello():
    name = "Robert"
    return "Witaj użytkowniku " + name + "!"


if __name__ == "__main__":
    app.run(debug=True)

