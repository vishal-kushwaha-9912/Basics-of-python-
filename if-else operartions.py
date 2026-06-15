# IF-ELSE operation is used to 

# LOGIN PAGE

 # correct gmail : vishalk4455@gmail.com
 # correct password : 445566vishu
 
email = input("Enter your email id : ")
if '@' in email :
 password = input("Enter your password :")
 
 if  email == "vishalk4455@gmail.com" and password == "445566vishu":
      print ("login successful")
 elif  email == "vishalk4455@gmail.com" and password != " 445566vishu":
      print ("password incorrect")
      password = input("enter your password again : ")
      if password =="445566vishu":
          print("finally correct ")
      else :
          print ("still incorrect password")
       
 
    
else :
      print ( "incorrect deatails")