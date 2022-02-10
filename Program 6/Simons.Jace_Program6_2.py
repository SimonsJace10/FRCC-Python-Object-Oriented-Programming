# declare the file_name as words.txt
file_name = "../files/mbox-short.txt"
# instantiate words as an empty dictionary
words = {'Sun': 0, 'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0}


# function to store the words from the file in a dictionary
def store_words():
    for line in open_file(file_name):
        if line.startswith("From"):
            temp_str = line.split()
            word = temp_str[2]
            print(word)
            # take the 3rd word and store it
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


store_words()
print(words)
