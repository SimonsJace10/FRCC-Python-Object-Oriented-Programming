# the hoursPrompt and salaryPrompt are the strings for prompting the user
hoursPrompt = "Input the number of hours worked\n"
salaryPrompt = "Input the pay rate\n"
# the hoursInput and SalaryInput store the user's input
hoursInput = input(hoursPrompt)
salaryInput = input(salaryPrompt)

# try ...
try:
    # casting the inputs to ints
    hours = int(hoursInput)
    salary = int(salaryInput)
    # if the hours is over 40 ...
    if hours > 40:
        # ... the pay is 100% of the salary for the first 40 hours and 150% for every hour after that
        pay = (salary * 40) + (hours - 40) * salary * 1.5
    else:
        # ... otherwise, the pay just equals the salary * hours
        pay = salary * hours
# if an exception is thrown ...
except:
    # ... tell the user that the input couldn't be casted to an int
    print('Non numeric. Please enter a number')
    # ... and exit the program
    exit()

# finally, print the total pay
print("Total pay is: " + str(pay))
