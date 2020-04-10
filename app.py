from flask import Flask, redirect, url_for, render_template
from flask_restful import Api
from resources.todo import Todo
app = Flask(__name__)
api = Api(app)

api.add_resource(Todo, "/todo/<int:id>")
@app.route("/")
def home():
    return render_template("htmlss.html", content="Testing", x=4)
if __name__ == "__main__":
  app.run()