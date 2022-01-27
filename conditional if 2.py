x = int(input("give a number: "))
y = int(input("give a number: "))

if(x % 2 == 0):
    if(y % 2 == 0):
        print("both number even")
    else:
        print("one of the numbers is even")
else:
    if(y % 2 == 0):
        print("one of the numbers is even")
    else:
        print("both number odd")
