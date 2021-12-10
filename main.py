import random

#functions
def howManyElements():
    elementCount = int(input("How manny elements will there be?\t"))
    if elementCount > 10:
        print("There cant be more than 10 inputs")
        howManyElements()
    print("Are you shure about having", elementCount, "elements?\n")
    confirmElementCount = input("Yes(Y)/No(N)\t")

    if confirmElementCount == "y":
        entries = []
        for i in range(0, elementCount):
            print("-", i+1)
            boxValue = input("Value:")
            entries.insert(0, boxValue)
        print(entries)
        print(random.choice(entries))
        exit()
    elif confirmElementCount == "Y":
        entries = []
        for i in range(0, elementCount):
            print("-", i+1)
            boxValue = input("Value:")
            entries.insert(0, boxValue)
        print(entries)
        print(random.choice(entries))
        exit()
    elif confirmElementCount == "n":
        howManyElements()
    elif confirmElementCount == "N":
        howManyElements()
    else:
        print("Invalid input!")
        howManyElements()


#run functions

howManyElements()

