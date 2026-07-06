# Level 1 – break (Logic)
# Q1.

# Search for 25 in the list.

# numbers = [10, 15, 20, 25, 30, 35]

# Print "Found" and stop searching.


numbers = [10, 15, 20, 25, 30, 35]
for number in numbers:
    if number == 25:
          break
   
    print(number)
   


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q2.

# Create a number guessing game.

# The computer's secret number is:

# secret = 17

# Keep asking until the user guesses correctly.

# When guessed correctly:

# Print "Correct!"
# Stop the loop.

# #output ::


secret =17


user = int(input("Enter the number :"))
while user != secret :
    if user <secret:
        print("guess higher ")
    else:
        print ("guess lower")
    
    user =int( input("guess the number : ")) 
  
print (" correct guess")       



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 🟠 Level 2 – break + continue
# Q3.



# Print numbers from 1 to 100.

# Skip all even numbers.
# Stop when the number becomes 75.

for x in range(1,101):
    if x%2 == 0:
        continue
    
    if x == 75:
       break
    print(x)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q4.

# Loop through:

# "Data Science"
# Skip all spaces.
# Stop when you reach "S".

for x in " Data Science":
    if x == " ":
        continue
    if x == "S" :
        break
    print(x)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q5.

# Take numbers from the user.

# Rules:

# Ignore all negative numbers.
# Stop when the user enters 999.
# Store only valid numbers in a list.

number =[]
while True:
    user = int(input("Enter the number : " ))
    if user < 0 :
        continue
    if user == 999:
        break
    number.append(user)
print("Valid number : ", number)







# 🔴 Level 3 – Better Logic

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q6.

# Take numbers from the user until they enter 0.

# Store only even numbers.

# Print the final list. >>

number =[]
while True:
    user = int(input("Enter the number :"))
   
    if user == 0:
        number.append(user)
        break
    if user % 2 != 0:
        continue
    number.append(user)
print(f"final list {number}")
        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q7.

# Password Checker

# Correct password:

# python123

# Rules:

# Empty input → continue
# Wrong password → ask again.
# Correct password → break

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q8.

# Take 10 numbers.

# Store only numbers divisible by 5.

# Skip all others.

number = []
for x in range(10):
    user = int(input("Enter the number :"))
    if user % 5 == 0 :
        number.append(user)
    else :
        continue
print(f"Number : {number}")



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 🔥 Level 4 – Nested Loops


# Q9.

# Print multiplication tables from 1 to 5.

# Stop printing the current table when multiplication reaches 7.


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q12.

# Shopping Cart

# Keep asking for item names.

# Empty input → continue
# "done" → break
# Store all valid items in a list.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q13.

# Student Marks

# Take marks of 10 students.

# -1 → Student absent → continue
# 999 → Stop entering marks → break

# Store only valid marks.


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q14. ⭐ Best Logic Question

# Create a menu:

# 1. Add Student
# 2. Delete Student
# 3. Show Students
# 4. Exit

# Requirements:

# Empty name → continue
# Invalid menu → continue
# Delete Student → use pass
# Exit → break
# Store student names in a list.
# Show all students when option 3 is selected.



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# ⭐ Challenge Questions
# Q19.

# Print numbers from 1 to 50.

# Skip multiples of 4
# Stop if the number is divisible by 19





# Q20.

# Write a simple ATM menu using a while loop.

# Menu:

# 1. Deposit
# 2. Withdraw
# 3. Balance
# 4. Exit

# Requirements:

# If the user enters an invalid option, use continue.
# If the user selects 4, use break.
# Use pass in a placeholder for a future Transfer Money feature.



