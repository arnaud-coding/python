from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/hello/<string:name>")
def hello(name: str):
    return render_template("hello.html", name=name)


@app.route("/devices")
def devices():
    return render_template("devices.html")


@app.route("/device-data")
def device_data():
    return render_template("device-data.html")


# simple server-side redirect example
@app.route("/goto-devices")
def goto_devices():
    return redirect(url_for("devices"))
