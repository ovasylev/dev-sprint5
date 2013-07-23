import os
import flask, flask.views
import scrabble
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

app.secret_key = "gfdcj"

@app.route("/")
def hello():
	return render_template("index.html", string="", result="")


@app.route("/scrabble", methods=["POST"])
def addNums():
	
	val = request.form["string"]
	#print val	
	#flask.flash(val)

	res = scrabble.scrabble('test.txt', 8)

	for i in res:
		flask.flash(i)

	return render_template("index.html", string="", result="")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
