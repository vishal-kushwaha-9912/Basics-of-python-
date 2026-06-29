# there are two types of type conversion in python : 


## 1 Implicit type conversion : it is a type conversion which is done by the python interpreter automatically.
# It is also known as type casting. It is done when we perform operations on different data types. 
# The python interpreter converts the data type of one operand to another operand's data type to perform the operation.

#example of implicit type conversion

#x = 10         # x is integer
#y = 3.14       # y is float
#z = x + y      # z is a float because the python interpreter converts the integer x to a float to perform the addition operation.
#print(z)    # output: 13.14



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..




#2 Explicit type conversion : it is a type conversion which is done by the programmer explicitly using the built-in functions.

#example of explicit type conversion
#x = 10         # x is integer
#y = 3.14       # y is float
#z = int(x+y)     # z is an integer because we explicitly convert the float y to an integer using the int() function.
                  # int (y) will give you 3 because it will remove the decimal part of the float.
#print(z)    # output: 13