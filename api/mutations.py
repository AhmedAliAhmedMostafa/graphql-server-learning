from datetime import datetime

from .models import Todo
from . import db

def resolve_create_todos(obj,info,description,dueDate):
  try:
    due_date = datetime.strptime(dueDate, '%d-%m-%Y').date()
    todo = Todo(description=description, due_date = due_date)
    db.session.add(todo)
    db.session.commit()
    
    return {
      "success":True,
      "todos":[todo.to_dict()]
    }
  except Exception as error:
    return {
    "success":False,
    "errors":[str(error)]
    }
def resolve_mark_done(obj, info, id):
  try:
    todo = Todo.query.get(id)
    todo.completed = True
    db.session.commit()
    
    return {
      "success":True,
      "todos":[todo.to_dict()]
    }
  except Exception as error:
    return {
    "success":False,
    "errors":[str(error)]
    }
def resolve_delete_todo(obj, info, id):
  try:
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    
    return {
      "success":True,
      "deleted_id":id
    }
  except Exception as error:
    return {
    "success":False,
    "errors":[str(error)]
    }
