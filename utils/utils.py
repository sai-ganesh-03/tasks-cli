import json
import os

from .todo import Todo
from .status import Status

file_name="todos.json"
current_directory = os.getcwd()
json_path=os.path.join(current_directory, file_name)

def dict_to_todo(dict):
    """
    Converts a dictionary to a Todo object

    Args:
        dict 

    Returns:
        Todo : Todo object
    """
    return Todo(id=dict["id"],description=dict["description"],status=Status(dict["status"]),created_at=dict["created_at"],updated_at=dict["updated_at"])
  
def todo_to_dict(todo):
    """
    Converts a Todo object to a dictionary

    Args:
        todo (TODO) : Todo object

    Returns:
        dict : dictionary representation of the Todo object
    """
    return {
        "id": todo.id,
        "description": todo.description,
        "status": todo.status.value,
        "created_at": todo.created_at,
        "updated_at": todo.updated_at
    }  

def deserialize():
    """
    Deserializes the todo list from the JSON file

    Returns:
        list : list of Todo objects
    """
    if not os.path.isfile(json_path):
        with open(json_path,"w") as f:
            json.dump([], f)
            
    todo_list = []
    with open(json_path,"r") as f:
        todos=json.load(f)
        
        for todo_dict in todos:
            todo_list.append(dict_to_todo(todo_dict))
            
    return todo_list

def serialize(todo_list):
    """
    Serializes the todo list to the JSON file

    Args:
        todo_list : list of Todo objects
        
    Returns:
        list : list of Todo objects
    """
    todo_dicts = [todo_to_dict(todo) for todo in todo_list]
    with open(json_path,"w") as f:
        json.dump(todo_dicts, f)


def add_todo(todo_description):
    """
    Adds a new todo to the json file

    Args:
        todo_description (str)

    Returns:
        int: Todo Id
    """
    todo_list=deserialize()
    if not todo_list:
        id=0
    else:
        id=max(todo_list, key=lambda todo: todo.id).id+1
        
    todo=Todo(id=id,description=todo_description)
    
    todo_list.append(todo)
    serialize(todo_list)    
    return todo.id

def list_todos(status):
    """
    Lists all the todos based on the provided status

    Args:
        status (str) : status of the todos

    Returns:
        str : formatted string of todo list
    """
    todo_list=deserialize()
    todo_list_str="ID -- Description -- Status \n"
    for todo in todo_list:
        if (not status) or todo.status.value==status:
            todo_list_str+=f"{todo.id} -- {todo.description} -- {todo.status.value} \n"
    return todo_list_str

def delete_todo(id):
    """
    Deletes the todo with the provided id from the json file

    Args:
        id (int) : id of the todo to be deleted

    Returns:
        int : deleted todo id
    """
    todo_list=deserialize()
    todo_list=list(filter(lambda todo:todo.id != id,todo_list))
    serialize(todo_list)  
    return id  

def update_todo_description(todo_id,todo_description):
    """
    Updates the description of the todo with the provided id in the json file

    Args:
        todo_id (int) : id of the todo
        todo_description (str) : new description of the todo

    Returns:
        int : todo id
    """
    todo_list=deserialize()
    for todo in todo_list:
        if todo.id==todo_id:
            todo.update_description(todo_description)
            serialize(todo_list)
            return todo.id
    
    return None
    
def update_todo_status_progress(todo_id):
    """
    Updates the status of the todo with the provided id to "In Progress" in the json file

    Args:
        todo_id (int) : id of the todo

    Returns:
        int : todo id
    """
    todo_list=deserialize()
    for todo in todo_list:
        if todo.id==todo_id:
            todo.mark_inprogress()
            serialize(todo_list)
            return todo.id
    
    return None

def update_todo_status_done(todo_id):
    """
    updates the status of the todo with the provided id

    Args:
        todo_id (int): id of todo

    Returns:
        int: todo id
    """
    todo_list=deserialize()
    for todo in todo_list:
        if todo.id==todo_id:
            todo.mark_done()
            serialize(todo_list)
            return todo.id
    
    return None