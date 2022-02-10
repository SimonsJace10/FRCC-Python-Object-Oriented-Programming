# declare the file_name as words.txt
file_name = "../files/mbox-short.txt"
# instantiate words as an empty dictionary
words = {'Sun': 0, 'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0}


# function to store the words from the file in a dictionary
def store_words():
    # for every line ...
    for line in open_file(file_name):
        # ... if the line starts with 'From ' ...
        if line.startswith("From "):
            # ... split the word into a list
            temp_str = line.split()
            # ... and temp_str is set equal to the 3rd element in said list
            word = temp_str[2]
            # take the 3rd word and store it
            # check what day it is and increment the count of that day depending on which one it is
            if word == "Sun":
                words['Sun'] = words['Sun'] + 1
            elif word == 'Mon':
                words['Mon'] = words['Mon'] + 1
            elif word == 'Tue':
                words['Tue'] = words['Tue'] + 1
            elif word == 'Wed':
                words['Wed'] = words['Wed'] + 1
            elif word == 'Thu':
                words['Thu'] = words['Thu'] + 1
            elif word == 'Fri':
                words['Fri'] = words['Fri'] + 1
            elif word == 'Sat':
                words['Sat'] = words['Sat'] + 1
            else:
                print("none of the above")
        # otherwise continue
        else:
            continue


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
store_words()
# print out the dictionary
print(words)
