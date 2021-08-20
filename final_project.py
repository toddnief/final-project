
import tasks_helper
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Command Line Task Manager.')

    parser.add_argument('--add', 
                        type=str, 
                        help='Add a task to the task manager')
    parser.add_argument('--due', 
                        type=str, 
                        help='Add a due date to a task')
    parser.add_argument('--priority', 
                        type=int, 
                        help='Add a priority to a task, Options are 1,2,3.')

    parser.add_argument('--delete', 
                        type=int,
                        help="Remove a task from the task list.")

    parser.add_argument('--done', 
                        type=int,
                        help="Mark a task as complete. Use unique ID as input.")

    parser.add_argument('--list',
                        action='store_true',
                        help="List tasks.")
    parser.add_argument('--report',
                        action='store_true',
                        help="List tasks.")

    parser.add_argument('--query',
                        type=str,
                        required=False,
                        nargs="+",
                        help="Search for tasks.")

    # Execute the parse_args() method
    args = parser.parse_args()

    all_tasks = tasks_helper.Tasks()

    if args.add:
        all_tasks.add(args)
    elif args.list:
        all_tasks.list()
    elif args.delete:
        all_tasks.delete(args.delete)
    elif args.query:
        all_tasks.query(args)
    elif args.done:
        all_tasks.done(args.done)
    elif args.report:
        print(all_tasks)

    # Pickle all tasks
    all_tasks.pickle_tasks()

# Make your task manager program an executable program. This will allow it to be run from any location on your computer. You will need to place a copy of it in a place where $PATH is looking for executable files. Research to find out where command line applications are typically stored (this will vary betweren Macs, Linus and Windows). You will also need change the running mode of the file (ie. chmod) and add a shebang line. You will also need to change the location of the users .pickle file so that it can be accessed from anywhere. Store it as an invisible file in the users home directory.

# Write the instructions for how you can accomplish this in a README.md file in your repository.