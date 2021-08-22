#!/Users/toddnief/opt/anaconda3/bin/python

import tasks_helper
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Command Line Task Manager')

    parser.add_argument('--add', 
                        type=str,
                        required=False,
                        help='Add a task to the task manager. Accepts --due and --priority as well.')
    parser.add_argument('--due', 
                        type=str,
                        required=False,
                        default = None,
                        help='Add a due date to a task')
    parser.add_argument('--priority', 
                        type=int,
                        required=False,
                        default = 1,
                        help='Add a priority to a task, Options are 1,2,3.')

    parser.add_argument('--delete', 
                        type=int,
                        required=False,
                        help="Remove a task from the task list by Task ID.")

    parser.add_argument('--done', 
                        type=int,
                        required=False,
                        help="Mark a task as complete by Task ID.")

    parser.add_argument('--list',
                        action='store_true',
                        required=False,
                        help="List incomplete tasks.")
    parser.add_argument('--report',
                        action='store_true',
                        required=False,
                        help="Print detailed tasks report. Includes completed tasks.")

    parser.add_argument('--query',
                        type=str,
                        required=False,
                        nargs="+",
                        help="Search for tasks by input string.")

    # Execute the parse_args() method
    args = parser.parse_args()

    all_tasks = tasks_helper.Tasks()

    if args.add:
        all_tasks.add(args.add, args.priority, args.due)
    elif args.list:
        all_tasks.list()
    elif args.delete:
        all_tasks.delete(args.delete)
    elif args.query:
        all_tasks.query(args.query)
    elif args.done:
        all_tasks.done(args.done)
    elif args.report:
        all_tasks.report()

    # Pickle all tasks
    all_tasks.pickle_tasks()
    exit()

# parser = argparse.ArgumentParser(description='Update your ToDo list.')
# # Add an argument
# parser.add_argument('--add', type=str, required=False, help='a task string to add to your list')
# parser.add_argument('--due', type=str, required=False, help='due date in dd/MM/YYYY format')
# parser.add_argument('--priority', type=int, required=False, default=1, help="priority of task; default value is 1")
# parser.add_argument('--query', type=str, required=False, nargs="+", help="priority of task; default value is 1")
# parser.add_argument('--list', action='store_true', required=False, help="list all tasks that have not been completed")

# # Parse the argument
# args = parser.parse_args()

# # Read out arguments (note the types)
# print("Add:", args.add)
# print("Due:", args.due)
# print("Priority:", args.priority)
# print("List:", args.list)