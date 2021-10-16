Max_Guess = 3
Saved_Number = 9
guess=int(input("Guess :--"))
No_of_Guesses = 1
while guess!=Saved_Number and No_of_Guesses<Max_Guess :
    guess=int(input("Guess :--"))
    No_of_Guesses+=1
else:
    if guess==Saved_Number:
        print("You won")
    else:
        print("You lost")