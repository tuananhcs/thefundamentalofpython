def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def missmatch_divezero(): 
    try:
        result = divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error: {e}")    

def missmatch_datatype(): 
    try:
        x = 10
        y = '2'
        z = x + y  # Trying to add an integer and a string
    except Exception as e:
        print(f"An error occurred: {e}")

def ex8():
    missmatch_divezero()
    missmatch_datatype()