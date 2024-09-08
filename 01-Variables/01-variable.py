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
server_names = ["Java", "Python", ".net"]
server_names.extend(server_names)
new_list= server_names[0:2]
print(server_names)
print(server_names[1]) # prints 2nd element. first element starts with Zero
print(len(server_names)) # length i.e how many elements are there.
print(new_list) # new list with 0 & 1 elements are created, 2 won't
   # numbers sorting
numbers = [2, 1, 101, 91, 51]
numbers.sort()
print(numbers)

    # Random values, List can store any data types-number,string etc 
random_values = ["krishna", '1', "DB", 2.3, "True" ]
print(random_values)

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
e=x%y # Modulo division means getting remainder
print(z)
print(w)
print(e)
