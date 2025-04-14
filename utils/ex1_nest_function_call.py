# Ham long trong ham
def create_multiplier(factor):
    """Returns a function that multiplies its input by the given factor."""
    def multiplier(x):
        return x * factor
    return multiplier

def ex1():
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    # Use the created functions
    print(double(5))  # Output: 10
    print(triple(5))  # Output: 15
