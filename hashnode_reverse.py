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

#method