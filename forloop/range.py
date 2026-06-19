# range(start, stop, step)


# Parameters :::
    
# start → Number to start from (default is 0)

# stop → Number to stop before

# step → How much to increase each time (default is 1) 
                 #OR
#  step →means how much to jump each time. 

# EXAMPLE 1 :: 
list(range(4)) # start

output : [0, 1, 2, 3]
  
# EXAMPLE 2:: 
list(range(1,6)) # range(start , stop) 

output : [1, 2, 3, 4 ,5]
    
#EXAMPLE 3:: 
list(range(1,10,2)) # range(start , stop , step)  # step = step means how much to jump each time. 

output : [1, 3, 5, 7, 9] jumped by 2 

# How it works 

# Start = 1
# Stop = 10 (10 is not included)
# Step = 2 (jump by 2)
         
         
         #NOTE :: WE CAN ALSO WRITE THE PRINT THE NUBER IN REVERSE 
         
list(range(12,0,-1))         
         
OUTPUT :: [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# Explanation ::
# Start = 12
# Stop = 0 (0 is not included)
# Step = -1 (go backwards by 1)        

list(range(12,0,-2))   

# Output ::[12 , 10, 8, 6 , 4 , 2]



# How Python  ::
# Start = 12
# Stop = 0 (0 is not included)
# Step = -2 (go backwards by 2)


### SEQUENCE 

numbers = [10, 20, 30, 40]


###list 
State =["uttarpradesh", "bihar", "assam", "gujarat"]



List → [1, 2, 3]
String → "Python"
Tuple → (1, 2, 3)
Range → range(5)