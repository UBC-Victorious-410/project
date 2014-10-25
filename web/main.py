import json
import flask
import os

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")

if __name__ == "__main__":
    port = 8080
    
    os.system("open http://localhost:{0}/".format(port))

    app.debug = True
    app.run(port=port)
