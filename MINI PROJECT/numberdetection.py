# 🚀 Mini Project: Number Detective
# Story

# Imagine you're a detective investigating a mysterious number. The user enters one number, and your program generates a complete "investigation report" about it.

# For example:

# 

# Digits: 2
# Sum of digits: 10
# Reverse: 82
# Largest digit: 8
# Smallest digit: 2
 
 


user_input = int(input("Enter Number :"))
print("=" * 40)
print("        NUMBER REPORT")
print("=" * 40)
# SIGN OF NUMBER 
if user_input > 0:
    print(f" Positive Number :{user_input} ")

elif user_input < 0:
     print(f" Negative number :{user_input}")

else :
    print(f"{user_input} is  Zero ")

        # NUMBER IS EVEN / ODD 
        
if user_input %2 == 0:
    print(f"Even Number  :{user_input}")
    
else :
    print(f"ODD Number   :{user_input}")
    
    # NUMBER IS DIVIDED BY 2/3/5/7
    
if user_input %2 == 0:
    print(f"Divided by 2 : YES ")
else:
    print((f"Divided by 2 : NO"))
        
if user_input %3 == 0:
    print(f"Divided by 3  :YES")
else:
    print((f"Divided by 3 : NO"))
    
if user_input %5 == 0:
    print(f"Divided by 5  : YES")
else:
    print((f"Divided by 5 : NO"))
    
if user_input %7 == 0:
    print(f"Divided by 7  :YES")
else:
    print((f"Divided by 7 : NO"))
    
    #  FIND SQUARE/CUBE
    
print(f"Square is :{user_input**2}")

print(f"Cube is :{user_input**3}")

#  FACTORIAL 

result =1
for x in range(1,user_input+1):
    result = result*x
print(f"Factorial is : {result}")
    
print("=" * 40)