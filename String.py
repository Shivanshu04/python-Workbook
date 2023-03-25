# defining the string
S1 ='Shivanshu' # use single quote

S2 = "Shivu" # use double quote
print(type(S1))
print(type(S2))

# use triple quote to create docstring / multiline strings
a = '''hello i am shivanshu gupta
i build most sucessful statrup in india
and provide lots of jobs in india
and featured in forbes under 30'''
print(a) #multiline String

#for new line we use \n
a = "Shivanshu\nGupta"
print(a)

#acessing the character in string
s= 'hello'
print(s[0])
print(s[3])
print(s[4])
 # negative  indexingp
print("anothe method")
s= 'hello'
print(s[-2])
print(s[-3])
print(s[-4])

# string Concatenation 
#We can perform string concatenation using the following ways:
#  1. Using + operator 
# 2. Using join() method
#  3. Using % operator
#  4. Using format() function

# Python program to demonstrate  # string concatenation
a="love"
b="you"
  # % Operator is used here to combine the string stored in var1 and var2 
print("%s %s" % (a, b))

#In Python, formatters work by employing replacement fields and different placeholders defined by a pair of curly braces {}, one curly brace for each string, and then calling {}.format().
#  The value we wish to concatenate is passed as function parameters to format(). Syntax : { } .format(value) Parameters : 
# (value) : Can be an integer, floating-point, string, characters or even variables containing other values.
#  Return type : Returns a formatted string with the value passed as a parameter in the placeholder position.
# Python3 program to demonstarte # the str.format() method # using format option in a simple string 
print ("{}, is best for DSA content." .format("CodingNinjas")) # using format option for a # value stored in a variable str = "This article is provided at {}" 
print (str.format("CodeStudio")) # formatting a string using a numeric constant
print ("Hello, I am {} years old".format(20))

# repeating the string
S= "Shivu"
print(S*3)
# reverse the string
a= "kids"
print(a[::-1])