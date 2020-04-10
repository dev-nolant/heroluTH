from flask import Flask, redirect, url_for, render_template
from flask_restful import Api
from resources.todo import Aapi
app = Flask(__name__)
api = Api(app)

api.add_resource(Aapi, "/api/<int:id>")
@app.route("/")
def home():
    return render_template("test.html", content="Testing", x=4)
if __name__ == "__main__":
  app.run()