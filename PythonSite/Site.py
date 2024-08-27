from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("StartList.html")

@app.route("/godot")
def index2():
	return render_template("godot.html")

@app.route("/godot/y2")
def index3():
	return render_template("godo_y2.html")

app.run(debug=True)