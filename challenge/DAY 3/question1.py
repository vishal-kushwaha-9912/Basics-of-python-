# Question 1: For Loop + If-Else (Medium)
# Find prime numbers

# Write a program that finds and prints all prime numbers between 1 and 20.
# (Hint: A prime number is only divisible by 1 and itself)

for x in range(2,21):
    is_prime = True
    
    for i in range(2,x):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        print(x)    
    
         
         