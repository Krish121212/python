import sys # sys(module) is used to read the Cmd line args

def add(num1, num2): 
    add= num1 + num2
    return add 

def sub(num1, num2):
    sub= num1 - num2
    return sub

def mul(num1, num2):
    mul= num1 * num2
    return mul

num1= float(sys.argv[1]) # so three cmd lin arg need to be given in "python 05-c* 20 add 20"
operation= sys.argv[2]
num2= float(sys.argv[3])

# to call the function
if operation == "add":
    output = add(num1, num2)
    print(output)