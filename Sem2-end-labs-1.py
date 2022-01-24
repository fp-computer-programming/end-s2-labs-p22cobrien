# Author: CMOB 1/19/2022

def greet(name):
    #add name to a greeting statement
    return("Hello, {0} how are you doing today?".format(name)) #takes variable and inputs it into string, then return


print(greet('Ryan') == "Hello, Ryan how are you doing today?")
print(greet(9) == "Hello, 9 how are you doing today?")
print(greet('john') == "Hello, john how are you doing today?")