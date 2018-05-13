# a program where the player and the computer trade places in the number guessing game.
# That is, the player picks a random number between 1 and 100 that the computer has to guess. Before you start, think about how you guess. If all goes well, try coding the game.

import random

number = (random.randrange(100)+1)
guess = int(input("Enter your guess: "))
trials = (1)

while (guess != number):
    if (guess > number):
        guess = int(input("Enter your guess lower: "))
    if (guess < number):
        guess = int(input("Enter your guess higher: "))
    trials += (1)

print ("The actual number is", number)
print ("You got it right in", trials, " trials!")

guess1 = int(input("Enter your guess: "))
number1 = (random.randrange(100)+1)
trials1 = (1)

while (number1 != guess1):
    if (number1 > guess1):
        number1 = (random.randrange(100)+1)
        print ("Computer, take lower number.")
    if (number1 < guess1):
        number1 = (random.randrange(100)+1)
        print ("Computer, take higher number.")
    trials1 += (1)

print ("Your guess is", guess1)
print ("Computer got it right in", trials1 , " trails!")

if (trials1 > trials):
    print \
          ("""
   ----    ----   -------    --   --          ---                        ---  ---    ---         ---
   \   \  /   /  |       |  |  | |  |         \   \                    /   / |   | |     \      |  |
    \   \/   /   |  ---  |  |  | |  |          \   \                  /   /  |   | |  |\  \     |  |
     \      /    | |   | |  |  | |  |           \   \       --       /   /   |   | |  | \  \    |  |
      \    /     | |   | |  |  | |  |            \   \    /    \    /   /    |   | |  |  \  \   |  |
       |  |      | |   | |  |  | |  |             \   \  /      \  /   /     |   | |  |   \  \  |  |
       |  |      | |   | |  |  | |  |              \   \/   /\   \/   /      |   | |  |    \  \ |  |
       |  |      |  ---  |  |   -   |               \      /  \      /       |   | |  |     \  \|  |
       |  |      |       |  |       |                \    /    \    /        |   | |  |      \     |
        --        -------    -------                   ---      ---           ---   --          ---
        """)
if (trials1 < trials):
    print \
          (""" 
  ---      ---    ---------    --   --         --           -------    ---------     ---------
  \   \  /   /   |         |  |  | |  |       |  |        |         | |   ______ |  |         | 
   \   \/   /    |   ---   |  |  | |  |       |  |        |   ---   | |  |          |  -------
    \      /     |  |   |  |  |  | |  |       |  |        |  |   |  | |  |          |  |
     \    /      |  |   |  |  |  | |  |       |  |        |  |   |  | |   -------   |   ------
      |  |       |  |   |  |  |  | |  |       |  |        |  |   |  |  ________   | |         |
      |  |       |  |   |  |  |  | |  |       |  |        |  |   |  |          |  | |   ------
      |  |       |   ---   |  |   -   |       |   ______  |   ---   |  _______ |  | |   |
      |  |       |         |  |       |       |         | |         | |           | |    ----- |
       --         ---------    -------         ---------    -------    -----------   ----------
       """)
    
