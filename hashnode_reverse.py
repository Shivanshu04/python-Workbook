# ways reverse to a string
# Method 1 - using Slice notation
def reverse_string (str):
    return str[::-1]
my_txt = reverse_string(" i am going to mumbai")
print(my_txt)

#method 2 using reverse function
def reverse_string(str):
    return ''.join(reversed(str))
my_txt =reverse_string("how")
print(my_txt)

#method 3 :- by using loop method
def reverse_string(str):
    new_str = ''
    for i in range(len(str)-1, -1, -1):
        new_str += str[i]
    return new_str
#method 4:- by using recursion
def reverse_string(str):
    if len(str) == 0:
        return str
    else:
        return reverse_string(str[1:]) + str[0]
#mrthod 5:- by using while loop
def reverse_string(str):
    new_str = ''
    i = len(str)-1
    while i >= 0:
        new_str += str[i]
        i -= 1
    return new_str
#method 6 :- using list comprehension

def reverse_string(str):
    return ''.join([str[i] for i in range(len(str)-1, -1, -1)])

# the slice notation method (Method 1) and the reverse function method (Method 2) are likely to be the most efficient ways to reverse a string in Python.