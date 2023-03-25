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