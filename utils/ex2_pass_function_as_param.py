# Truyen Function as Param
def apply_operation(operation, x, y):
    return operation(x, y)

# Functions to pass as arguments
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def ex2(): 
# Using the higher-order function
    result_add = apply_operation(add, 3, 4)
    result_multiply = apply_operation(multiply, 3, 4)
    
    print(result_add)       # Output: 7
    print(result_multiply)  # Output: 12