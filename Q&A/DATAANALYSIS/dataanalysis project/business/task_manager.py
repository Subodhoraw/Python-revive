"""task manager"""
from datetime import datetime
class Task:
    """ A class to manage individual tasks"""
    def __init__(self,title,priority ="Medium"):
        self.title = title
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    def mark_complete(self):
        self.complete = True
        return f"Task completed 😁{self.title}"
    def mark_incomplete(self):
        self.complete = False
        return f"Task not completed yet 😟: {self.title }"
    def get_status(self):
        return "completed😁" if self.completed else "not yet 😟"
    def display(self):
        """display task details """
        status = self.get_status()
        priority_symbol = "🔴" if self.priority =="High" else "🟡"  if self.priority =="Medium" else "🟢"
        return f"{status} {priority_symbol} {self.title} [{self.priority}] - created :{self.created_at}"
class TaskManager:
    """A class to manage multiple tasks"""
    def __init__(self,owner):
        self.owner = owner
        self.tasks = []
    def add_task(self,title,priority = "Medium"):
        """add a new task"""
        task = Task(title,priority)
        self.tasks.append(task)
        return f"added {title}"
    def completed_task(self,index):
        """mark task as completed"""
        if 0 <= index < len(self.tasks):
            return self.tasks[index].mark_complete()
        return "invalid Task number"
    def get_pending(self):
        """count incomplete task"""
        return sum(1 for task in self.tasks if not task.completed)        
    def display_all(self):
        """display all tasks"""
        print(f"\n{'='*60}")
        print(f"Task list - {self.owner}")
        print(f"{'='*60}")
