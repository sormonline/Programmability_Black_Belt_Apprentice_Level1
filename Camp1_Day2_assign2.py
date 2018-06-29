import random
guess = random.randint(1, 10)
while(True):
    print("Guess the number: ", end="")
    number = int(input())
    if number == guess:
        print("Correct!")
        break
    else:
        print("Wrong, try again!")  