
from functools import reduce


def map_func():
    numbers = [1,2,3,4,5,6] 
    doubled_number = list(map(lambda x: x*2, numbers))
    return doubled_number

def reduce_func(): 
    numbers = [1,2,3,4,5,6] 
    sum = reduce(lambda x, y: x+y, numbers)
    return sum

def map_func2(): 
    strings = ['hello', 'world', 'python']
    lengths = list(map(len, strings))
    return lengths

def map_func3(): 
    numbers = [1,2,3,4,5,6]
    squared_even = list(map(lambda x: x*2, filter(lambda x: x%2 == 0, numbers)))
    return squared_even

def reduce_func2(): 
    numbers = [10, 20, 5, 40, 30]
    product = reduce(lambda x, y: x if x > y else y, numbers)
    return product

def ex6(): 
    print(map_func())
    print(reduce_func())
    print(map_func2())
    print(map_func3())
    print(reduce_func2())





