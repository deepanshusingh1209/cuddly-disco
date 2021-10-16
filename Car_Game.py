print("welcome to the car game :) :) ")
beginning = input(">")
options = ["start - to start the car" , "stop - to stop the car" , "quit - to exit"]
if beginning == "help":
    for items in options:
        print(items)
    option_1 = input("choose one: ")
    if option_1 == "start":
        print("car started... ready to go!!")
    elif option_1 == "stop":
        print("Car Stopped...")
    elif option_1 == "quit":
        print("Game Quitted... Bye:)")
    else:
        print("i don't understand that")
else:
    print("earlier what you said was wrong command :-) \nNow Start the game again :-- :-)")
    for items in options:
        print(items)
    option_1 = input("choose one: ")
    if option_1 == "start":
        print("car started... ready to go!!")
    elif option_1 == "stop":
        print("Car Stopped...")
    elif option_1 == "quit":
        print("Game Quitted... Bye:)")
    else:
        print("i don't understand that")