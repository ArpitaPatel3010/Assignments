#How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.
#ANS An exception in Python is an incident that happens while executing a program that causes the regular course of the program's commands to be disrupted. When a Python code comes across a condition it can't handle, it raises an exception. An object in Python that describes an error is called an exception.When a Python code throws an exception, it has two options: handle the exception immediately or stop and quit.

def div(num):
    try:
        divide = 1/num
    except ZeroDivisionError as err:
        print("You cant divide zero to a num")
    else:
        print(divide)
    
div(2)
div(0)