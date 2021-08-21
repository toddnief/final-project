For Mac, we store the command line applications in /usr/local/bin

We can confirm that this is part of our $PATH by typing $PATH into the command line and making sure that our directory shows up.

We need to make sure that all of our users have read and execute permissions. We can do this with the following command:
sudo chmod a+rx /path/to/final_project.py

We also need to add a shebang line to make sure the file is being executed with the proper version of Python. In this case, we use the Anaconda build of Python found here:
#!/Users/toddnief/opt/anaconda3/bin/python

Then, we move our final_project.py file into /usr/local/bin

The pickled tasks are saved as a hidden file in the user's home directory.