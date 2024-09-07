# Data Types
str1 = "Krishna"
str2 = "Kishore"
result = str1 + " " + str2
print(result)

a=10
b=3.24
print(a,b)

# Python is case sensitive in booleon True and true are different.
c= True
print(c)

# String
a= 'This is Krishna'
b= "This is also Krishna"
c= """
This is multi line string
"""
# when to use which string. d fails(hence i gave \ - it acts as escape sequence), e runs
d= 'I\'m krishna'
print(a,b,c,d)

# List
server_names = ["DB", "Backend", "Frontend"] # can add more to list, mutable
server_names.append("backend2")
server_names.remove("Backend")
print(server_names)
print(server_names[1]) # prints 2nd element. first element starts with Zero
print(len(server_names)) # length i.e how many elements are there.


# Tuple
tuple_test = ( "krishna", "kishore", "Malladi", "db" ) # can't add more to tuple, immutable
print(type(tuple_test))

# Dict
test_dict = {'a': 1, 'b': 2}
print(test_dict)

# Set
# consider the values in an arbitrary way
test_set = {'a', 'b', "abc"}
print(test_set)

# type() function --> prints the data type of the variable.
print(type(server_names))

# Operations
# Add, Sub, Multi - not writing for this

# Divide 
x=100
y=5
z=x/y # By default answer would be float data type
w=x//y # int value will come
print(z)
print(w)

# Modulo division meanss getting remainder







