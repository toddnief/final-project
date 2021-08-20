from datetime import date
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
        self.completed = 0
        self.created = date.today()

        if priority==1 or priority==2 or priority==3:
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

class Tasks:
    """A list of `Task` objects."""

    def __init__(self):
        """Read pickled tasks file into a list"""
        self.pickle_name = ".todo.pickle"

        self.tasks = []

        # read pickled tasks. Create pickle file if file not found.
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
        """Print tasks in columns."""
        print("ID\tAge\tDue Date\tPriority\tTask")
        print("--\t---\t--------\t--------\t----")
        for task in self.tasks:
            if task.completed == 0:
                print(f"{task}")

# Task Report Command
# List all tasks, including both completed and incomplete tasks, using the report command. Follow the formatting shown below for the the output. Follow the same reporting order as the --list command.

# $ python todo.py report

# ID   Age  Due Date   Priority   Task                Created                       Completed
# --   ---  --------   --------   ----                ---------------------------   -------------------------
# 1    3d   4/17/2018   1         Walk dog            Mon Mar  5 12:10:08 CST 2018  Mon Mar  5 12:10:08 CST 2018
# 2    10d  3/20/2018   3         Study for finals    Tue Mar  6 12:10:08 CST 2018  Tue Mar  6 12:10:08 CST 2018
# 3    1d   -           2         Buy eggs            Tue Mar  6 12:10:08 CST 2018  -
# 4    30d  -           1         Make eggs           Tue Mar  6 12:10:08 CST 2018  -
# Note: This action will be useful for debugging and testing the completed and deleted commands.

    def report(self):
        pass

    def done(self, id):
        """Find task by id and mark as done."""
        i = 0
        for task in self.tasks:
            if task.id == id:
                task.completed = 1
                print(f"Completed Task {id}")
                break
            i += 1
        if i == len(self.tasks):
            print(f"Could not find task with id {id}")
        return

# Task List Command Using a Query Term
# Search for tasks that match a search term using the --query command. Only return tasks are not completed in your results.

# $ python todo.py --query eggs

# ID   Age  Due Date   Priority   Task
# --   ---  --------   --------   ----
# 3    1d   -           2         Buy eggs
# 4    30d  -           1         Make eggs

# Muliple terms should be able to be searched. The argparse package allows you to pass in multiple values for a single argument using nargs='+':

# parser.add_argument('--query', type=str, required=False, nargs="+", help="priority of task; default value is 1")
# For example:

# $ python todo.py --query eggs dog

# ID   Age  Due Date   Priority   Task
# --   ---  --------   --------   ----
# 1    3d   4/17/2018   1         Walk dog
# 3    1d   -           2         Buy eggs
# 4    30d  -           1         Make eggs

    def query(self, args):
        query_matches = []
        for query in args.query:
            for task in self.tasks:
                if query in task.name:
                    query_matches.append(task)
        return query_matches

    def delete(self,id):
        """Find task by id and delete it."""
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

# Task Add
# Add a new task by using the --add command. Examples of adding tasks are shown below.

# Note that the task description needs to be enclosed in quotes if there are mulitple words. argparse should provide sufficient error handling for user input, however you need to test that the data matches the type expected.

# The unique identifier is returned when the operation is successful. If the operation is not successful, inform the user and end the program. Remember that the due date is optional. If a priority is not given, then assign it a default value of 1.

# $ python todo.py --add "Walk Dog" --due 4/17/2018 --priority 1
# Created task 1

# $ python todo.py --add 2 --due 4/17/2018 --priority 1
# There was an error in creating your task. Run "todo -h" for usage instructions.

# $ python todo.py --add "Study for finals" --due 3/20/2018 --priority 3
# Created task 2

# $ python todo.py --add "Buy milk and eggs" —due friday --priority 2
# Created task 3

# $ python todo.py --add "Cook eggs"
# Created task 4

    def add(self, args):
        """Add task to task list. Create task id one larger than current largest task id."""
        # Create task object with task name.
        name = args.add
        task = Task(name)

        # Set task value for priority and due date if arguments provided.
        if args.priority:
            task.priority = args.priority
        if args.due:
            task.due = args.due

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