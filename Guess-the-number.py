import random

n = random.randrange(1,1000) #a random select from range one and a thousand

guess = int(input("Enter any number between one and a thousand: ")) #collects user input after printing string

while n!= guess: 

    if guess < n:
        print("your number is too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("you guessed it right!")
