# Day 1 of the Advent
# of coding challenge

with open('input.txt','r') as file: # Import list of string from file
        data = file.readlines()

def mostCalories():

    calories = 0        # Calorie addition variable
    elfCalories = list()    # List of the elves calorie totals

    for x in data:      # For loop to check each elf and their calories

        if x == '\n':   # If the string is a newline, append the calorie amount
                        # to the list of elf calories

            elfCalories.append(calories)
            calories = 0

        else:           # If the string had an integer in it, add 
                        # add the integer to calories

            calories += int(x.strip())      # Strip the string to get rid of any non
                                            # numerical characters and make the string
                                            # an integer

    return sorted(elfCalories)  # Return the list of the elves calories

def topElvesFunct(elfCalories):
    topElves = 0
    for i in range(1,4):
        topElves += elfCalories[len(elfCalories) - i] 
    return topElves


if __name__ == "__main__":
    elfCalories = mostCalories()
    topElves = topElvesFunct(elfCalories)

    # Part 1
    print(elfCalories[len(elfCalories) - 1])
    
    # Part 2
    print(topElves)
