import random
secret_number = random.randint(1, 100)
guess = None
tries = 0
print("welocme to the number guessing game")
print("i have picked a number between 1 and 100.can you guess?")
while guess != secret_number:
    try:
        guess = int(input("enter your guess: "))
        tries += 1
        if guess < secret_number:
            print("Too low!! Try again")
        elif guess > secret_number:
            print("too high!!.Try agian")
        else:
            print(f"Correct! you guessed it in {tries} tries")
    except ValueError:
        print("plese enter a valid number") 
