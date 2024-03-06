"""
Create a file named number_guess.py
Import the random module
Prompt the user to enter a number between 1 and 10. Save the guess as a variable of type integer.
Generate a random number between 1 and 10 using the random.randrange() method and save as a variable named number.
Track the number of guesses using a variable named count.
Create a while loop and test if the guess variable doesn't match the random number variable.
Within the while loop block, increment the count to track the number of guesses.
Within the while loop block, prompt the user to guess again and assign the input as an integer to the guess variable.
Finally, print a success message stating the correct number guessed and the number of tries to guess it.
Upload your file to your GitHub and send me the link.
"""

import random
count = 0
number = 0
guess = 0
number = random.randrange(1, 11)

while guess != number:
    count += 1
    guess = int(input('Guess a number between 1 and 10: '))
    if guess == number:
        print(f'Yes! the number chosen is {number} in {count} tries')
        break

    else:
        print(f'Nope! Try Again! The answer is not guess {guess}')