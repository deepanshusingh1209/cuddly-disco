Saved_Number = 6
Guess01 = int(input("Guess01 :--")) 
if Guess01 == Saved_Number:
    print("You won")
else:
    Guess02 = int(input("Guess02 :--"))
    if Guess02 == Saved_Number:
        print("You won")
    else:
        Guess03 = int(input("Guess03 :--"))
        if Guess03 == Saved_Number:
            print("You won")
        else:
            print("You lost")
            
