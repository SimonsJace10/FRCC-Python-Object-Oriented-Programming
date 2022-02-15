# declare the file_name as words.txt
file_name = "../files/mbox-short.txt"
# instantiate dictionary with letters a-z and initial count of 0
letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
           'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, }


def extract_letters():
    # for every line ...
    for line in open_file(file_input()):
        # for every character ...
        for char in line:
            # instantiate new variable to be the lowercase version of the char
            analysis_char = char.lower()
            # if the char is alphanumeric
            if analysis_char.isalpha():
                # increment its value in the dictionary
                letters[analysis_char] += 1
        else:
            continue


# hour frequency finally prints out the totals for each hour
def letter_frequency():
    for item in letters:
        print(item + ': ' + str(letters[item]))


# prompt user to input file name
def file_input():
    print('Input file name')
    return '../files/' + input()


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


# call the function
extract_letters()
# print out the dictionary
letter_frequency()
