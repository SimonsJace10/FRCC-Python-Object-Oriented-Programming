# creating vars
# hoursPrompt and salaryPrompt are the strings for prompting the user
hoursPrompt = "Input the number of hours worked\n"
salaryPrompt = "Input the pay rate\n"
# the hoursInput and salaryInput are for storing the input from their respective prompts, and subsequently casting them
# to ints
hours = int(input(hoursPrompt))
salary = int(input(salaryPrompt))

# if the hours worked are more than 40 ...
if hours > 40:
    # ... the total pay will be the salary times 40, PLUS 150% of the salary for every extra hour over 40
    pay = (salary*40) + (hours - 40)*salary*1.5
# otherwise ...
else:
    # ... the total pay will just be the salary times hours
    pay = salary*hours

# print the total pay
print("Total pay is: " + str(pay))
