import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "This is the {} application.".format(os.environ.get("APP"))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
