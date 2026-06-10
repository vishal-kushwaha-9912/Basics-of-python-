# we take input from the user and print it .

##In input first we declare a variable to store the  value. then we use input function to take input from the user and store in a variable.

#  name = input("what is your name? ")

first_number = input("enter the first number: ")
second_number = input("enter the second number: ")

sum = int(first_number) + int(second_number)  
print("the sum of the two numbers is :", sum)

# WE can also take input in a single line and split it into multiple variables using the split() method.
x, y = input("enter two numbers separated by space: ").split()
x = int(x)
y = int(y)
print("the sum of the two numbers is :", x + y)