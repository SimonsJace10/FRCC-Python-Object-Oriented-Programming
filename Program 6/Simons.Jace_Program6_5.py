# declare the file_name as words.txt
file_name = "../files/mbox-short.txt"
# instantiate emails as dictionary of domains
emails = {'gmail.com': 0, 'media.berkeley.edu': 0, 'iupui.edu': 0, 'caret.cam.ac.uk': 0, 'umich.edu': 0, 'uct.ac.za': 0}


# function to store the words from the file in a dictionary
def store_words():
    # for every line ...
    for line in open_file(file_name):
        # ... if the line starts with 'From ' ...
        if line.startswith("From "):
            # ... split the word into a list
            temp_line = line.split()
            # then take the 2nd word from that list
            temp_email = temp_line[1]
            # then split that word at @
            temp_str = temp_email.split('@')
            # ... and temp_str is set equal to the 2nd word, which is the domain after the @
            word = temp_str[1]
            # check what domain it is and increment it depending on which one it is
            if word == 'gmail.com':
                emails['gmail.com'] += 1
            if word == 'media.berkeley.edu':
                emails['media.berkeley.edu'] += 1
            if word == 'iupui.edu':
                emails['iupui.edu'] += 1
            if word == 'caret.cam.ac.uk':
                emails['caret.cam.ac.uk'] += 1
            if word == 'umich.edu':
                emails['umich.edu'] += 1
            if word == 'uct.ac.za':
                emails['uct.ac.za'] += 1
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
print(emails)
