from flask import Flask, render_template, request, redirect, url_for
import dbhelper

app = Flask(__name__)

@app.route("/")
def home():
	try:
		data = dbhelper.get_all_inputs()
	except Exception as e:
		print(e)
		data = None
	return render_template("home.html", data=data)
	
@app.route("/add", methods=["POST"])
def add():
	try:
		data = request.form.get("userinput")
		dbhelper.add_input(data)
	except Exception as e:
		print(e)
	return redirect(url_for("home"))

@app.route("/clear")
def clear_all():
	try:
		dbhelper.clear_all()
	except Exception as e:
		print(e)
	return redirect(url_for("home"))

@app.route("/clear/<id_>")
def clear(id_):
	try:
		dbhelper.clear(id_)
	except Exception as e:
		print(e)
	return redirect(url_for("home"))
	
if __name__ == "__main__":
	app.run(debug=True)

