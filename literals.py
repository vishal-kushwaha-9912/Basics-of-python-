# literals : Literals are fixed values that are written directly in the source code.
#there are three types of litrals in python :

#1 number literals
#2 string literals
#3 booleans literals
#speach literals

#Number literals : it is a fixed value that represents a number. It can be an integer, a float, or a complex number.
#example of number literals
a = 10       # Integer literal
b = 3.14     # Float literal
c = 2 + 3j   # Complex literal



a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
#   c = 00310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3

#Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2,float_3)
print(x, x.imag, x.real)

""" OUTPUT : 
10 100 200 300
10.5 150.0 0.0015
3.14j 3.14 0.0"""




# string literals : it is a fixed value that represents a sequence of characters. It can be enclosed in single quotes, double quotes, or triple quotes.


#example of string literals
str1 = 'Hello, World!' # Single quotes
str2 = "Hello, World!" # Double quotes
str3 = '''Hello, World!''' # multiple line string literal
unicode = u"\u00A9" # Unicode string literal print copyright symbol : u"\u00A9"
smiley = u"\u263A" # Unicode string literal print smiley face : u"\u263A"
raw_str = r"C:\Users\Name\Documents" # Raw string literal

print(str1)
print(str2)
print(str3)
print(unicode)
print(smiley)
print(raw_str)


#boolean literals : it is a fixed value that represents a boolean value. It can be either True or False.
#example of boolean literals
bool1 = True 
# there are sometimes is 1(true) and 0(false) in some programming languages but in python we use True and False)
bool2 = False

sum =bool1+1     # output is 2 because true is treated as 1 
sum2 = bool2+1  # output is 1 because false is treated as 0
print(bool1)
print(bool2)
print(sum)
print(sum2)



#specail literals : it is a fixed value that represents a special value. It can be None, Ellipsis, or NotImplemented.
                
                   ### NOTE : None is a special literal that represents the absence of a value.for an extra variable that is used in future code to declaread assign a value .
#example of special literals
none_literal = None
ellipsis_literal = ...
not_implemented_literal = NotImplemented
print(none_literal)
print(ellipsis_literal)
