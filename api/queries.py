from .models import Todo
def resolve_todos(obj, info):
  try:
    todos = [todo.to_dict() for todo in Todo.query.all()]
    print(todos)
    payload = {
      "success":True,
      "todos":todos
    }
  except Exception as error:
    payload = {
      "success":False,
      "errors":[str(error)]
    }
  finally:
    return payload
  

def resolve_todo(obj,info,id):
  try:
    todo = Todo.query.get(id).to_dict()
    payload = {
      "success":True,
      "todos":[todo]
    }
  except Exception as error:
    payload = {
      "success":False,
      "errors":[str(error)]
    }
  return payload




