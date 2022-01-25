# define the computegrade function which takes a score (float) as an argument
def computegrade(scorearg):
    # try ...
    try:
        # ... create a new variable which stores the argument casted to a float
        floatscore = float(scorearg)
        # if the casted score is less than or equal to 1.0 (100%)
        if floatscore <= 1.0:
            # if the score is greater than 90 ...
            if floatscore > 0.9:
                # it's an A
                return "A"
            # greater than 80
            elif floatscore > 0.8:
                # it's a B
                return "B"
            # and so on ...
            elif floatscore > 0.7:
                return "C"
            elif floatscore > 0.6:
                return "D"
            # if it's none of the above, its an F
            else:
                return "F"
        # if it's above 1.0 (100) ...
        else:
            # ... tell the user and exit the program
            print('Invalid score; try again')
            exit()
    except:
        # if an exception is thrown, tell the user and exit the program
        print('Invalid score; try again')
        exit()


# the string for the user prompt
scorePrompt = "Input the score as a decimal (ex: 95% would be inputted as 0.95)\n"
# store the input
score = input(scorePrompt)
# call the function and pass in the input
print(computegrade(score))
