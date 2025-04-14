# def outer_scope2(name, city):

#     def inner_scope():
#         print(f"Hello {name}, Greetings from {city}")

#     return inner_scope

# # Creating closures with different names and locations
# greet_priyanshu = outer_scope2('Dr Priyanshu', 'Jaipur')
# greet_sam = outer_scope2('Sam', 'New York')

# # Executing the closures
# greet_priyanshu()    # Output: Hello Dr Priyanshu, Greetings from Jaipur
# greet_sam()     # Output: Hello Sam, Greetings from New York