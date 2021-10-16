# Importing Library for Getting Random Number by a function
import random

# Loop Variable' so the user can play as long as he want.
Game = "yes"

# While Loop to Start The Game.
while Game == "yes":

    # List From the random number will be selected
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # User's Name
    name = input("Your Name : ")
    print("Let's Play {}\n".format(name))

    # random Number
    num = random.choice(lis)

    # for counting the guesses
    count = 3
    print("Iam Thinking of a number between 1 to 10! \nGuess That number in 3 Tries : \n")

    # using for loop so that it can count the tries
    for i in range(3):
        '''
        i have used if and else conditions to check and count guesses and even give hints if user is guessing
        wrong.
        
        Inputs :
        => guess 
        => name 
        
        In output it will tell us :
        => The hints (if user is guessing wrong )
        => guesses 
        => result ( if he won or lose)
        => wish to contiue
        '''
        choose = int(input("Your Guess : "))
        if num == choose:
            print("\n   you won the Game!\n")
            break
        else:
            count -= 1
            print("Wrong! {} guesses left".format(count))
            if choose > num:
                print("Think of a less number than that\n")
            if choose < num:
                print("Think of a higher number than that\n")
        if count == 0:
            print(" 'you Lost the Game' \n")

    # asking user if he want to continue or not.
    Game = input("Do you want to continue the game : Yes or No \n").lower()


