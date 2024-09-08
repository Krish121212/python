# strings
sample_string= "This is my sample string"

# single string
print(sample_string[9])

# slicing
print(sample_string[11:17])
 # for string we need to give start:end:step size --> But they are optional
print(sample_string[:]) # you can get complete string i.e "This is my sample string"
print(sample_string[5:]) # print started from 5th character as we specified starting point as 5
print(sample_string[:5]) # starting five letters will come as we specified end point as 5
print(sample_string[::2]) # starting,ending ae not specified - but step size is 2. so every two alternate alphabet will be printed
print(sample_string[::-1]) # reverse of string



# common functions used on a string - split(), Join(), format(), count(), strip()

sample_string= "This is my sample string"
# split
sample_split= sample_string.split()
print(sample_split, type(sample_split)) # split will always get an output of LIST type

# join
sample_join= " ".join(sample_split)
print(sample_join, type(sample_join))






