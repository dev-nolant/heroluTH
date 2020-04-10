from flask_restful import Resource

todos = [
  {
    "id": 133244223123,
    "item": "Welcome :)",
    "status": "End Game"
  }
]

class Todo(Resource):
  def get(self, id):
    for todo in todos:
      if(id == todo["id"]):
        return todo, 200
    return "Item not found for the id: {}".format(id), 404

  def put(self, id):
    for todo in todos:
      if(id == todo["id"]):
        todo["item"] = request.form["data"]
        todo["status"] = "Open"
        return todo, 200
    return "Item not found for the id: {}".format(id), 404