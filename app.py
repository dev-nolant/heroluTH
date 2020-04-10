from flask import Flask
from flask_restful import Api
from resources.todo import Todo
import json
with open("resources\test.json", 'r') as f:
    distros_dict = json.load(f)
app = Flask(__name__)
api = Api(app)

api.add_resource(Todo, "/todo/<int:id>")

if __name__ == "__main__":
  app.run()