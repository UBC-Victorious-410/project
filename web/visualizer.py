import json
import flask
import os

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")

def begin():
	port = 8080
	os.system("open http://localhost:{0}/".format(port))
	app.debug = True
	app.run(port=port)

if __name__ == "__main__":
  	begin()
