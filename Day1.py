# Day 1 of the Advent
# of coding challenge

with open('input.txt','r') as file: # Import list of string from file
        data = file.readlines()

def mostCalories(data):

    calories = 0        # Calorie addition variable
    mostCalories = 0    # Variable to be set as the current most calories

    for x in data:      # For loop to check each elf and their calories

        if x == '\n':   # If the string is a newline, check to see if the
                        # elf had the most calories

            if calories > mostCalories:     # If the elf had more calories
                mostCalories = calories     # than the previous mostCalories, 
                calories = 0                # replace mostCalories & reset calories
            else:
                calories = 0                # Reset calories

        else:           # If the string had an integer in it, add 
                        # add the integer to calories

            calories += int(x.strip())      # Strip the string to get rid of any non
                                            # numerical characters and make the string
                                            # an integer

    return mostCalories # Return the amount of calories the coolest elf has


if __name__ == "__main__":
    print(mostCalories(data))
