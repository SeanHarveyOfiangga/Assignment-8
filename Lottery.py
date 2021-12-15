#Program 1: Lottery
#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.

import random

# intro
def intro():
    print("\n\033[47m\033[30m**Welcome to Lottery App**\033[0m")
intro()

#user bet input
def lottobet():
    #instruction
    print("""\n\033[01m0-9 LOTTO BETTING INSTRUCTION:\033[0m
    \033[01m\033[36m>>\033[0m Enter your \033[32mthree number combination\033[0m from \033[04m0-9\033[0m as your bet
    \033[01m\033[36m>>\033[0m Winners will receive \033[93m5,000,000 PHP\033[0m
    """)
    entry = 1
    combination = []
    while entry <= 3:
        try:
            bet = int(input(f"\033[33mEnter your bet number " + str(entry) + ": \033[0m"))
        except ValueError:
            print("\033[91mERROR! You entered an invalid value.\n\033[0m")
            continue
        if bet >= 10:
            print("\033[91mYour bet is over the limit, please enter your bet again.\n\033[0m")
        if bet not in combination:
            combination.append(bet)
        else:
            print("\033[91mOops! You already picked this number.\n\033[0m")
            continue 
        entry += 1
    return combination

#winning combination generator
def winningcombi():
    win = []
    combi = random.sample(range(0,9),3)
    win.append(combi)
    return win

#win checker - checks if your bet is same with the winning combination
def winchecker(bet, win):
    print("\nYour bet combination is:\033[32m", bet,'\033[0m')
    print("The winning combination is:\033[32m", win,'\033[0m')
    if bet == win:
        print("Congratulations!")
        print("You win 5,000,000 PHP")
    else:
        print("\nThat was quite close.")

#try again loop
def tryagain():
    while True:
        tryagain = input("\n\033[95mWant to try again?:\033[0m ").lower()
        if tryagain[0] == 'y':
            print("\nThis is it, you'll get it this time.")
            print("Good luck!")
            main()
        if tryagain[0] == 'n':
            print("\n\033[47m\033[30mMaybe luck is not on your side this time")
            print("Try again next time, Bye!\033[0m")
            exit()
        elif tryagain != 'yes' or 'no':
            print("Invalid input, please answer 'Yes' or 'No'")   
            continue

#main call function
def main():
    usercombi = lottobet()
    wincombi = winningcombi()
    winchecker(usercombi, wincombi)
    tryagain()

main()
