
# 1. **Pattern Printing – Pyramid of Numbers**:
# 
# Print a number pyramid where each row contains numbers from 1 up to the row number, 
# and the pyramid is centered using spaces (e.g., for 5 rows, row 3 looks like `  1 2 3`).

for x in range(1,6):
    space = 5-x
    for y in range(0,space):
        print(" ",end="")
    for y in range(1,x+1):
         print(y,end=" ")
    print()



# for x in range(1,6):
#     space = 5-x
#     for y in range(0, space):
#         print(" ",end="")
#     for y in range(0,x):
#          print("*",end=" ")
#     print()
"""    OUTPUT:: 
         
    *
   * *
  * * *
 * * * *
* * * * * 

"""

# 2. **Diamond Star Pattern**:
# Print a diamond shape made of stars (`*`), where the user inputs the number of rows for the upper half.



# 3. **Prime Numbers in a Range**:
# Given two numbers `a` and `b`, print all prime numbers between them using nested for loops 
# (outer loop for numbers, inner loop for checking divisibility).



# 4. **Armstrong Numbers in a Range**:
# Find and print all Armstrong numbers (numbers equal to the sum of their digits each raised to the power of the number of digits)
# between 1 and 10,000.



# 5. **Floyd's Triangle**:
# Print Floyd's Triangle up to `n` rows, where the triangle contains consecutive natural numbers arranged in a right triangle starting from 1.



# 6. **Pascal's Triangle**:
# Generate and print Pascal's Triangle up to `n` rows using nested loops (without using factorial functions, only loop logic).



# 7. **Spiral Matrix Printing**: 
# Given an `n x n` matrix, print all its elements in spiral order (starting from top-left, moving right, then down, then left, then up).



# 8. **Sum of Digits Until Single Digit (Digital Root)**:
# Using only loops (no recursion), reduce a number to a single digit by repeatedly summing its digits, and print each intermediate step.



# 9. **Pattern with Alternating Characters**:
# Print a square or rectangular pattern where characters alternate between two symbols
# (like a checkerboard pattern) using nested loops and conditional logic inside the loop.



# 10. **Number Pattern with Reverse Counting**:
# Print a pattern where each row first counts up from 1 to `n` and then counts back down to 1 (e.g., row 3 of 4 would look like `1 2 3 2 1`),
# forming a butterfly or hourglass-like number pattern.

