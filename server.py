from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route("/hello/")
def hello():
    local = datetime.now()
    return local.strftime("%H:%M:%S")


if __name__ == "__main__":
    app.run(debug=True)
