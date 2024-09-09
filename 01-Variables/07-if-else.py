import sys

type = sys.argv[1]

if type == "t2.micro":
    print("cost is 10rs per hour")
elif type == "t3.micro":
    print("cost is 15rs per hour")
elif type == "t4.micro":
    print("cost is 20rs per hour")
elif type == "t5.micro":
    print("cost is 25rs per hour")
else:
    print("enter a type")