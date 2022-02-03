# the string for prompting the user
file_name_prompt = "Input the name of a file\n"
# store the input
file_name = input(file_name_prompt)

# declare an empty list
spam_confidence_numbers_list = []


# define a function which takes a line number as an argument
def extract_number(line):
    # initialize a list to store the digits to later be converted into a string
    temp_str = list()

    # iterate through the characters in the string
    for character in range(0, len(line)):
        # if the character at hand is either a digit or a '.' ...
        if (line[character].isdigit()) | (line[character] == "."):
            # ... append the character to the list of characters
            temp_str.append(line[character])

    # store the number, by converting the list into a string and subsequently casting it into a float
    spam_confidence_number = float("".join(temp_str))
    # put the number into the end of the list of all of the extracted numbers
    spam_confidence_numbers_list.append(spam_confidence_number)


# define an open_file function, which takes the file_name from the top
def open_file(file_name):
    # try ...
    try:
        # ... opening the file
        file_handler = open(file_name)
        # tell the user that the current file is (file_name)
        print("Working file: " + file_name)
        # return the file_handler object to be used at the bottom
        return file_handler
    # if it throws an exception ...
    except:
        # tell the user and exit the program
        print("Invalid file name; try again")
        exit()


# define a compute average function
def compute_average():
    # the spam confidence average gets instantiated at zero
    spam_confidence_average = 0
    # along with count
    count = 0

    # iterate through the list of extracted numbers
    for i in spam_confidence_numbers_list:
        # increment the count
        count += 1
        # add the current number (casted as a float) to the running average calculation
        spam_confidence_average += float(i)

    # finally, calculate the average by dividing the total by the number of elements
    spam_confidence_average /= count
    # return said average
    return spam_confidence_average


# iterate through the lines in the file which is returned by the open_file function
for line in open_file(file_name):
    # if the given line starts with this pattern ...
    if line.startswith("X-DSPAM-Confidence:"):
        # ... run the extract_number function having passed in the line at hand
        extract_number(line)

# finally, print the average to the user by casting the average to a string
print("Average spam confidence: " + str(compute_average()))
