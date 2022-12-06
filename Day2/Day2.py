# Day 2 of the
# Advent of code

# Rock Paper Scissors Challenge

with open('input.txt','r') as file: # Import list of string from file
        data = file.readlines()

firstScore = 0
secondScore = 0
for x in data:
    # Variables
    opponent = (ord(x[0]) - ord('A'))   # Get the RPS value for the opponent
    user = (ord(x[2]) - ord('X'))       # Get the RPS value for the user
    winCondition = user                 # Get the outcome value of the RPS for the
                                        # second part

    # First Part
    if(user == opponent):               # If there is a tie, add three to the score
        firstScore += 3
    if(user == (opponent + 1) % 3):     # If there is a win, add six to the score
        firstScore += 6
    firstScore += (user + 1)            # Add the RPS score value to the score

    # Second Part
    secondScore += (winCondition * 3)   # Add the outcome score value
    if(winCondition == 2):              # Win? add the RPS value that would correspond
        secondScore += (opponent + 1) % 3 + 1
    if(winCondition == 1):              # Tie? Add the RPS value that would correspond
        secondScore += (opponent + 1)
    if(winCondition == 0):              # Lose? Add the RPS value that wouledd correspond
        if(opponent == 0):
            secondScore += 3
        secondScore += (opponent)

# Answers
print(firstScore)
print(secondScore)