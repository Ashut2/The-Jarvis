'''
The __name__ variable is a built-in variable that holds the name of the current module. When a script is run directly, its __name__ is set to "__main__".
The if __name__ == "__main__": block is often placed at the end of a script, but it can be located anywhere within the file.


Standalone Scripts: When you want a script to be run directly from the command line, placing the main execution logic within this block prevents it from running when the script is imported as a module in another program.
Testing and Debugging: It's often used for testing or debugging purposes, allowing you to run specific code snippets directly without affecting other parts of your application.
Module Initialization: You can use it to initialize variables or perform setup tasks that are only necessary when the module is run as the main program.


'''

"""

> after importing the modules 
> i make the recognizer object for recognizing whatever
user speak 
> Recognizer() - a class which helps us to acces recog. functionality

> listen() - this contains two parameters
first = timeout() and phase_time_limit()
timeout(2) - it will wait 2 sec for phrase to start.

"""
"""
hurdles 1 ::

sphinix was not installed hence 
when we tried to test it , it throughthe error

sol--->
we used stackoverflow for this issue and found out that the issue is :not installed

hurdle 2 : 
it was throwing runandwait error 
solN :
we transfered the timeout audio source varibale into the while true tab so that it can run again again
"""
