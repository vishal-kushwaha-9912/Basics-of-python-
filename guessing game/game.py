import random
jackport = random.randint(1,80)
 
 
guessnum =int( input("guess the number : "))
counter = 1
while guessnum != jackport :
    if guessnum <jackport:
        print("guess higher ")
    else:
        print ("guess lower")
    
    guessnum =int( input("guess the number : ")) 
    counter += 1
print (" correct guess")     
print(" number of attemptes : ", counter)  