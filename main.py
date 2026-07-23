# the perfect guesss

import random
n = random.randint(1,100)
a = -1
guesses = 0
limit = 7
while(a !=n):
    guesses += 1
    if(guesses<=limit):
        a = int(input("Guess the number(1 to 100):"))
        if(n>a):
           print("Higher number Please..")
        elif(n<a):
            print("Lower number Please..")    
    else:
        print("Game over Tryy next time")

    
print(f"You guess the number {n} in {guesses} attempts")