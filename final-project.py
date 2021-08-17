# The user should run the program completely from the command line passing in commands and arguments that will alter the behavior of the program. The commands are --add, --delete, --list, --report, --query, and --done. Use the argparse package to help with parsing the command line arguements.

# Each command will be followed with arguments, as seen in the following examples:

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

def add_task():
    pass

# Task List Command
# Use the --list command to display a list of the not completed tasks sorted by the due date. If tasks have the same due date, sort by decreasing priority (1 is the highest priority). If tasks have no due date, then sort by decreasing priority.

# Note that only tasks that are not completed should be listed with this command. The Age in the table is the number of days since the task was created.

# Follow the formatting shown below.

# $ python todo.py list

# ID   Age  Due Date   Priority   Task
# --   ---  --------   --------   ----
# 1    3d   4/17/2018   1         Walk dog
# 2    10d  3/20/2018   3         Study for finals
# 3    1d   -           1         Buy eggs
# 4    30d  -           2         Make eggs

def list_tasks():
    pass

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

def task_query():
    pass

# Task Done Command
# Complete a task by passing the done argument and the unique identifier. The following example complete tasks 1 and 2. Remember that you are not deleting a task, you are just marking it as complete. Your --list methods should ensure that it not longer is printed to the terminal.

# $ python todo.py --done 1
# Completed task 1

# $ python todo.py --done 2
# Completed task 2

# $ python todo.py --list

# ID   Age  Due Date   Priority   Task
# --   ---  --------   --------   ----
# 3    1d   -           2         Buy eggs
# 4    30d  -           1         Make eggs

def complete_task():
    pass

# Delete Command
# Delete a task by passing the --delete command and the unique identifier.

# $ python todo.py --delete 3
# Deleted task 3

# $ python todo.py list

# ID   Age  Due Date   Priority   Task
# --   ---  --------   --------   ----
# 4    30d  -           1         Make eggs

def delete_task():
    pass

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

def task_report():
    pass

# Make your task manager program an executable program. This will allow it to be run from any location on your computer. You will need to place a copy of it in a place where $PATH is looking for executable files. Research to find out where command line applications are typically stored (this will vary betweren Macs, Linus and Windows). You will also need change the running mode of the file (ie. chmod) and add a shebang line. You will also need to change the location of the users .pickle file so that it can be accessed from anywhere. Store it as an invisible file in the users home directory.

# Write the instructions for how you can accomplish this in a README.md file in your repository.