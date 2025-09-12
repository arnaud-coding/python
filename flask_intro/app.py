from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    ip = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<Device {self.name}>"


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/hello/<string:name>")
def hello(name: str):
    return render_template("hello.html", name=name)


@app.route("/devices", methods=["POST", "GET"])
def devices():
    if request.method == "POST":
        device_name = request.form["name"]
        device_ip = request.form["ip"]
        device_status = request.form["status"]
        new_device = Device(name=device_name, ip=device_ip, status=device_status)

        try:
            db.session.add(new_device)
            db.session.commit()
            return redirect("/devices")
        except:
            return "There was an issue adding your device"
    else:
        devices = Device.query.order_by(Device.id).all()
        return render_template("devices.html", devices=devices)


@app.route("/device-data")
def device_data():
    return render_template("device-data.html")


# simple server-side redirect example
@app.route("/goto-devices")
def goto_devices():
    return redirect(url_for("devices"))

@app.route("/addForm")
def addForm():
    return render_template("addForm.html")
