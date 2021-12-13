#Program 1: Lottery
#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.

def intro():
    print("\n\033[47m\033[30m**Welcome to Lottery App**\033[0m")
intro()

def userbet():
    print("""\n\033[01m0-9 LOTTO BETTING INSTRUCTION:\033[0m
    \033[01m\033[36m>>\033[0m For each bet you must pay \033[04m\033[95m20 PHP\033[0m
    \033[01m\033[36m>>\033[0m Enter your \033[32mthree number combination\033[0m from \033[04m0-9\033[0m as your bet
    \033[01m\033[36m>>\033[0m Winners will receive \033[93m5,000,000 PHP\033[0m
    """)
    entry = 1
    while entry <= 3:
        try:
            bet = int(input(f"\033[33mEnter your bet number " + str(entry) + ": \033[0m"))
        except ValueError:
            print("\033[91mERROR! You entered an invalid value.\n\033[0m")
            continue
        entry += 1
userbet()