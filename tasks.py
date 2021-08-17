# Each task should be able to be uniquely identified from all other tasks by a numeric identifier. Tasks should be assigned a priority level of 1, 2 or 3 to indicate the importance (3 is the highest priority).

# A Task object should store the date they were created and completed. In addition, the task manager should allows for different types of tasks: a task with no due date and a task with a due date.

class Task:
  """Representation of a task
  
  Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
  """
    pass

# Implement a Tasks objects that will contain all the Task objects. Tasks should be implemented as a list of Task objects. You may use the standard Python list() to hold you Task objects. The list should be ordered by the creation date (to improve search efficiency). While running, you program should only have a single instance of Tasks.

class Tasks:
   """A list of `Task` objects."""
   
    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks = [] 
        # your code here

    def pickle_tasks(self):
        """Picle your task list to a file"""
        # your code here

    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        pass

    def report(self):
        pass

    def done(self):
        pass

    def query(self):
        pass

    def add(self):
        pass

# All the Tasks data should be serialized to disk using Python pickle module. Write to a file named .todo.pickle in the same directory as your program. The . is not a typo. Prefixing a file with a . makes it an invisible file.

# This file will exist in a directory, but will not be visible to the user by default. This is a good practice when storing data in a file that you do not want the user to open or modify. See unix challenge on how to visualize invisible files.

# When your program exits, you should ensure that all tasks have been serialized to disk. When you program begins, you should ensure that all your tasks are loaded into objects from the serialized file.