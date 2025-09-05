from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/bonjour/<string:name>")
def bonjour(name: str):
    return render_template("bonjour.html", name=name)


@app.route("/devices")
def devices():
    return render_template("devices.html")


# simple server-side redirect example
@app.route("/goto-devices")
def goto_devices():
    return redirect(url_for("devices"))


# ...existing code...
