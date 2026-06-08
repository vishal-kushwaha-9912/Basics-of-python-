"""Question 5: Simple Calculator

Ask the user for two numbers and print:

Addition = ?
Subtraction = ?
Multiplication = ?
Division = ?"""

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

add =num1+num2
print("The Addition of two number is :",add)

sub =num1-num2
print("The Subtraction of two number is :",sub)

mul =num1*num2
print("The Multiplication of two number is :",mul)


if(num2 ==0):
    print("Division by zero is not possible")
else:
    div =num1/num2
    print("The Division of two number is :",div)












