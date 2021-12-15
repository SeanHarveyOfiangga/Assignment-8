#Program 2: Guess the number
#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.

import random

def intro():
    print("\n\033[47m\033[30m**Welcome to Guess the number app!**\033[0m")
intro()

def number():
    print("""\n\033[01mHow to play Guess the number?\033[0m
    \033[01m\033[36m>>\033[0m \033[33mRandom number from \033[04m0-100\033[0m will be generated and the user will guess what is the number.\033[0m
    \033[01m\033[36m>>\033[0m \033[33mThe program will say if the guess is higher or lower than the unknown number.\033[0m
    \033[01m\033[36m>>\033[0m \033[33mIf the guess matched the unknown number, user will be declared as the winner.\033[0m
    *********************************************************************************""")
    Name = input("I am Guess.bot and you are?: ")
    print(f"""\nHello {Name}, are you ready? Let's Start.
    Here is your unknown number: ?""")
    while True:
        try:
            guess = input("What is your guess?: ")
        except ValueError:
            print("Your answer is empty")
            continue      
number()