#Using python debugger
import pdb 

def divide(a, b):
    return a / b  # Might cause ZeroDivisionError

x, y = 10, 0  # Intentional error

pdb.set_trace()  # Start debugging
result = divide(x, y)
print(result)

"""
When the debugger starts, you'll get a (Pdb) prompt. You can then use commands like:

n - Next line
s - Step into function
c - Continue execution
q - Quit debugger
p variable - Print variable value
"""