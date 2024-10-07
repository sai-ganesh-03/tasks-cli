from .status import Status
from datetime import datetime

class Todo:
    """
    Represents a todo task.
    """
    @staticmethod    
    def get_current_time():
        return datetime.now().isoformat()
    
    def __init__(self,id, description,status=Status.Todo,created_at=get_current_time(),updated_at=get_current_time()):
        self.id = id
        self.description = description
        self.status = status
        self.created_at=created_at
        self.updated_at=updated_at
        
    def update_description(self,description):
        self.description = description
        self.updated_at=datetime.now().isoformat()
        
    def mark_inprogress(self):
        self.status = Status.In_Progress
        self.updated_at=datetime.now().isoformat()
        
    def mark_done(self):
        self.status = Status.Done
        self.updated_at=datetime.now().isoformat()
        
    def mark_todo(self):
        self.status = Status.Todo
        self.updated_at=datetime.now().isoformat()