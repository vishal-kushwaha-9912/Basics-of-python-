# WHILE LOOP :
#Definition :A while loop in Python is used to execute a block of code repeatedly as long as a given condition is True.



###Flow of Execution :

#The condition is checked.
#If the condition is True, the loop body executes.
#After execution, the condition is checked again.
#The loop continues until the condition becomes False.
#hen the condition is False, the loop stops.


###Uses of While Loop :

#Repeating tasks until a condition is met.
#Taking user input until valid data is entered.
#Menu-driven programs.
#Counting and iteration when the number of repetitions is not known beforehand.


number = int(input("Enter the number : "))
i =1


while  i<11 :
     print (number, "*",i,"=" ,number *  i) #(number*i) also write this 
     i += 1
     
     
# user input 75 
#output :      Enter the number : 75
#75 * 1 = 75
#75 * 2 = 150
#75 * 3 = 225
#75 * 4 = 300
#75 * 5 = 375
#75 * 6 = 450
#75 * 7 = 525
#75 * 8 = 600
#75 * 9 = 675
#75 * 10 = 750