# string to list conversion
sample_str = "This is Python and Im krishna"
sample_str_list = list(sample_str)
print(sample_str_list)

# string to tuple conversion
sample_str = "This is Python and Im krishna"
sample_str_list = tuple(sample_str)
print(sample_str_list)

# Accepting input from a user
user_input= input("Enter a number:-")
print(user_input, type(user_input)) # By default input will be of string type

add_88 = int(user_input) + 88 # Hence we need to change the type to int - if needed
print(add_88)