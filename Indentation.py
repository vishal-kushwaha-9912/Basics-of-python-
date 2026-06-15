#if condition:
    # code to execute if condition is True

#elif condition:
    # code to execute if the above condition is False
    # and this condition is True

#else:
    # code to execute if all conditions are False    
    
age = 18

if age > 18:
    print("Adult") #always used tab in python in the place used of space.
elif age == 18:
    print("Just became an adult")
else:
    print("Minor")