from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route("/hello/")
def hello():
    local = datetime.now()
    return local.strftime("%d-%m-%Y")


if __name__ == "__main__":
    app.run(debug=True)
