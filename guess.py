import random

secret = random.randint(1, 100)
tries = 0

print("Welcome to the number guessing game!")
print("I am thinking of a number from 1 to 100. Guess it in as few tries as you can.")

guess = 0
while guess != secret:
    guess = int(input("Your guess: "))
    if guess < 1 or guess > 100:
        print("Please guess from 1 to 100")
    else:
        tries += 1
        if guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            print("Correct! You took", tries, "tries.")

if tries <= 5:
    print("Amazing!")
elif tries <= 8:
    print("Good")
else:
    print("Keep practising")
