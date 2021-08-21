For Mac, we store the command line applications in /usr/local/bin

We can confirm that this is part of our $PATH

You will also need change the running mode of the file (ie. chmod) and add a shebang line. You will also need to change the location of the users .pickle file so that it can be accessed from anywhere. Store it as an invisible file in the users home directory.