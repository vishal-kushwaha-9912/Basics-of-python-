#""" #variable """ : it is a container for storing data values. It can hold different types of data such as numbers, strings, lists, etc. Variables are used to store and manipulate data in programming languages. 
# They can be assigned values and can be changed throughout the program.

#in python, you can assign values to multiple variables in a single line using the following syntax:
#variable1, variable2, variable3 = value1, value2, value3

#""" DYNAMIC TYPING """: In Python, you don't need to declare the type of a variable. The type is determined at runtime based on the value assigned to it. This means that you can change the type of a variable by assigning a different type of value to it.
# For example, you can assign an integer value to a variable and then later assign a string value to the same variable without any issues.

#""" DYNAMIC BINDING """: One variable can change DATA TYPES during the execution of a program.
#example of dynamic typing and dynamic binding

x = 10 # x is an integer
print(x) # output: 10
x = "hello" # x is now a string
print(x) # output: hello


#special synatax for multiple variable assignment


#""" 1 """
a, b, c = 1, 2, 3
print(a) # output: 1
print(b) # output: 2
print(c) # output: 3


#""" 2 """

a, b, c = 1, 2, 3
print(a, b, c) # output: 1 2 3

#""" 3 """

a = b = c = 1
print(a) # output: 1
print(b) # output: 1
print(c) # output: 1


