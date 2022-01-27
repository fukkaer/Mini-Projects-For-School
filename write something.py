keepgoing = True
while keepgoing:
    userwrote = input("write something: ")

    if userwrote == "quit":
        keepgoing = False
    else:
        print(userwrote)
