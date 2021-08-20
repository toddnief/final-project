# Each task should be able to be uniquely identified from all other tasks by a numeric identifier. Tasks should be assigned a priority level of 1, 2 or 3 to indicate the importance (3 is the highest priority).

from datetime import date
import time
import pickle
from dateutil import parser
from pathlib import Path

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
    def __init__(self, name, priority=None, due=None):
        self.name = name
        self.created = date.today()

        if priority:
            self.priority = priority
        else:
            self.priority = 1

        if due:
            self.due = parser.parse(due)
        else:
            self.due = "-"

    def __str__(self):
        self.age = date.today() - self.created
        print_version = str(self.id) + "\t" + str(self.age.days) + " days \t" + str(self.due) + "\t\t" + str(self.priority) + "\t\t" + str(self.name)

        return print_version

# Implement a Tasks objects that will contain all the Task objects. Tasks should be implemented as a list of Task objects. You may use the standard Python list() to hold you Task objects. The list should be ordered by the creation date (to improve search efficiency). While running, you program should only have a single instance of Tasks.

class Tasks:
    """A list of `Task` objects."""

    def __init__(self):
        """Read pickled tasks file into a list"""
        self.pickle_name = ".todo.pickle"

        # List of Task objects
        self.tasks = []

        try:
            self.tasks = pickle.load( open(self.pickle_name, "rb" ) )
        except:
            Path(self.pickle_name).touch()

        # sort tasks on creation date
        self.tasks.sort(key=lambda tsk: tsk.created)

    def pickle_tasks(self):
        """Pickle your task list to a file"""
        pickle.dump(self.tasks ,open(self.pickle_name,"wb" ))

    def list(self):
        print("ID\tAge\tDue Date\tPriority\tTask")
        print("--\t---\t--------\t--------\t----")
        for task in self.tasks:
            print(f"{task}")

    def report(self):
        pass

    def done(self):
        pass

    def query(self, args):
        query_matches = []
        for query in args.query:
            for task in self.tasks:
                if query in task.name:
                    query_matches.append(task)
        return query_matches

    def delete(self,id):
        i = 0
        for task in self.tasks:
            if task.id == id:
                self.tasks.pop(i)
                print(f"Deleted Task {id}")
                break
            i += 1
        if i == len(self.tasks):
            print(f"Could not find task with id {id}")
        return

    def add(self, task):
        self.tasks.append(task)
        task.id = len(self.tasks)
        return

# All the Tasks data should be serialized to disk using Python pickle module. Write to a file named .todo.pickle in the same directory as your program. The . is not a typo. Prefixing a file with a . makes it an invisible file.

# This file will exist in a directory, but will not be visible to the user by default. This is a good practice when storing data in a file that you do not want the user to open or modify. See unix challenge on how to visualize invisible files.

# When your program exits, you should ensure that all tasks have been serialized to disk. When you program begins, you should ensure that all your tasks are loaded into objects from the serialized file.