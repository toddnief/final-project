from datetime import datetime, timezone
import pickle
from dateutil import parser
from pathlib import Path
import os

def long_print(print_date):
    if isinstance(print_date, datetime):
        print_date = print_date.strftime("%a %b %-d %X ") + print_date.tzname() + print_date.strftime(" %Y")
    return print_date

def short_print(print_date):
    if isinstance(print_date, datetime):
        print_date = print_date.strftime("%b %-d %Y")
    return print_date

class Task:
    """Representation of a task

    Attributes:
                - created - date
                - completed - date
                - name - string
                - unique id - number - this is added when added to the tasks list
                - priority - int value of 1, 2, or 3; 1 is default
                - due date - date, this is optional
    """
    def __init__(self, name, priority, due):
        self.name = name
        self.completed = "-"
        self.created = datetime.now().astimezone()

        if priority==1 or priority==2 or priority==3:
            self.priority = priority
        else:
            # Print error message if invalid input for priority and assign default value.
            self.priority = 1
            print("Priority can only be 1,2, or 3. Priority set to default value of 1.")

        if due:
            try:
                self.due = parser.parse(due)
            except:
                self.due = "-"
                print("Unknown due date format. Due date left empty.")

    def __str__(self):
        self.age = datetime.now().astimezone() - self.created
        print_version = str(self.id).ljust(4, " ") + str(self.age.days) + " days".ljust(8," ") + str(short_print(self.due)).ljust(15, " ") + str(self.priority).ljust(10," ") + str(self.name)

        return print_version

class Tasks:
    """A list of `Task` objects."""

    def __init__(self):
        """Read pickled tasks file into a list"""
        self.pickle_name = ".todo.pickle"
        self.home = str(Path.home())
        self.pickle_file_path = os.path.join(self.home, self.pickle_name)

        self.tasks = []

        # read pickled tasks. Create pickle file if file not found.
        try:
            self.tasks = pickle.load( open(self.pickle_file_path, "rb" ) )
        except:
            Path(self.pickle_name).touch()

        # sort tasks on creation date
        self.tasks.sort(key=lambda tsk: tsk.created)

    def pickle_tasks(self):
        """Pickle your task list to a file"""
        pickle.dump(self.tasks ,open(self.pickle_file_path,"wb" ))

    def list(self):
        """Print tasks in columns."""
        headers = "ID".ljust(4, " ") + "Age".ljust(9," ") + "Due Date".ljust(15, " ") + "Priority".ljust(10," ") + "Task"
        print(headers)
        dividers = "--".ljust(4, " ") + "---".ljust(9," ") + "--------".ljust(15, " ") + "--------".ljust(10," ") + "----"
        print(dividers)
        for task in self.tasks:
            if task.completed == "-":
                print(f"{task}")

    def report(self):
        """Print detailed reports of tasks including date created. Includes completed tasks."""
        headers = "ID".ljust(4, " ") + "Age".ljust(9," ") + "Due Date".ljust(15, " ") + "Priority".ljust(10," ") + "Task".ljust(25, " ") + "Created".ljust(30, " ") + "Completed"
        print(headers)

        dividers = "--".ljust(4, " ") + "---".ljust(9," ") + "--------".ljust(15, " ") + "--------".ljust(10," ") + "----".ljust(25, " ") + "----------".ljust(30, " ") + "----------".ljust(15, " ")
        print(dividers)

        for task in self.tasks:
            if task.completed == "-":
                completed_string = "-"
            else:
                completed_string = long_print(task.completed)

            print_string = str(task).ljust(63," ") + long_print(task.created).ljust(30," ") + completed_string.ljust(15," ")
            print(print_string)

        return

    def done(self, id):
        """Find task by id and mark as done."""
        i = 0
        for task in self.tasks:
            if task.id == id:
                task.completed = datetime.now().astimezone()
                print(f"Completed Task {id}")
                break
            i += 1
        if i == len(self.tasks):
            print(f"Could not find task with id {id}")
        return

    def query(self, queries):
        query_matches = []
        for query in queries:
            for task in self.tasks:
                if query.lower() in task.name.lower():
                    query_matches.append(task)

        if query_matches == []:
            print("No tasks found.")
        else:
            headers = "ID".ljust(4, " ") + "Age".ljust(9," ") + "Due Date".ljust(15, " ") + "Priority".ljust(10," ") + "Task"
            print(headers)
            dividers = "--".ljust(4, " ") + "---".ljust(9," ") + "--------".ljust(15, " ") + "--------".ljust(10," ") + "----"
            print(dividers)
            for task in query_matches:
                if task.completed == "-":
                    print(f"{task}")
        return

    def delete(self,id):
        """Find task by id and delete it."""
        i = 0
        for task in self.tasks:
            if task.id == id:
                self.tasks.pop(i)
                print(f"Deleted Task {id}")
                break
            i += 1
        if i == len(self.tasks) and len(self.tasks) != 0:
            print(f"Could not find task with id {id}")
        return

    def add(self, name, priority, due):
        """Add task to task list. Create task id one larger than current largest task id."""
        # Create task object with task name.
        task = Task(name, priority, due)

        # Initialize task IDs at 1. Otherwise increment by 1 from largest current ID.
        if self.tasks == []:
            largest_id = 0
        else:
            largest_id = max(task.id for task in self.tasks)
        task.id = largest_id + 1

        # Add new task to tasks list.
        self.tasks.append(task)

        print(f"Created Task {task.id}")
        return