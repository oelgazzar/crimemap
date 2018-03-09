import json
from flask import Flask, render_template, request, redirect, url_for
import dbhelper

app = Flask(__name__)

@app.route("/")
def home():
	crimes = dbhelper.get_all()
	crimes = json.dumps(crimes)
	return render_template("home.html", crimes=crimes)
	
@app.route("/submitcrime", methods=["POST"])
def submitcrime():
	try:
		data = request.form
		dbhelper.add_crime(data)
		# print(data)
	except Exception as e:
		print(e)
	return redirect(url_for("home"))

if __name__ == "__main__":
	app.run(debug=True)

