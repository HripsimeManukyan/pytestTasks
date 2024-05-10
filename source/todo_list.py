# todo_list.py

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def mark_task_completed(self, task):
        if task in self.tasks:
            self.tasks[self.tasks.index(task)] += " (completed)"

    def get_tasks(self):
        return self.tasks
