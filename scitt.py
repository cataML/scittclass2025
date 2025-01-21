"""  Please make sure you read the entire README.md file to follow the instructions. 
You dont have to follow how I have started the game. Please use your creativity """
import random
sec_num = random.randint(1, 10)
count = 0

#Introduction to the game and what the game is all about.
print("Welcome to the Number Guessing Game!")
pass

print("\nThe program has selected a number between 1 and 10. Please guess the number")

#The game: A loop that enables the users to guess the numbers untill they get it right.
while True:
    try:
        guess = int(input("\nEnter your guess here: "))

#This counts the guesses users make during the game until they get it right.      
        count += 1

#This is the output if the user guess a higher number than expected.  
        if guess > sec_num:
            print("Too high! Try again")

#This is the output if the user guess a lower number than expected.
        elif guess < sec_num:
            print("Too low! Try again")

#This is the output if the user guess the correct number.
        else:
            print(f'\nCongratulations! You guessed the number in {count} attempts')

#This ends the game after the user guess a correct number        
            break
   
#This the output when a guess is not an integer.
    except ValueError:
        print("Invalid input! Please enter a valid number")

