from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")

def index(path):
	try:	
		if path.endswith(('.html', '.css')): 
			return render_template("%s" % path, error="200/OK"), 200

		elif ('//' in path) or ('~' in path) or ('..' in path):
			return render_template('403.html', error="403/Forbidden"), 403

		else:
			return render_template('404.html', error="404/NOT_FOUND"), 404
	except:
		return render_template('404.html',error="404/NOT_FOUND"), 404

@app.errorhandler(403)

def error_403(error):
	return render_template("403.html", error="403/Forbidden"), 403

@app.errorhandler(404)

def error_404(error):
	return render_template("404.html",error="404/NOT_FOUND"), 404

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
