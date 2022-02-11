# declare the file_name as words.txt
file_name = "../files/mbox-short.txt"
# instantiate emails as a list of emails
emails = {'gopal.ramasammycook@gmail.com': 0, 'louis@media.berkeley.edu': 0, 'cwen@iupui.edu': 0,
          'antranig@caret.cam.ac.uk': 0, 'rjlowe@iupui.edu': 0, 'gsilver@umich.edu': 0, 'david.horwitz@uct.ac.za': 0,
          'wagnermr@iupui.edu': 0, 'zqian@umich.edu': 0, 'stephen.marquard@uct.ac.za': 0, 'ray@media.berkeley.edu': 0}

# function to store the words from the file in a dictionary
def store_words():
    # for every line ...
    for line in open_file(file_name):
        # ... if the line starts with 'From ' ...
        if line.startswith("From "):
            # ... split the word into a list
            temp_str = line.split()
            # ... and temp_str is set equal to the 3rd element in said list
            word = temp_str[1]
            # take the 2nd word and store it
            # check what day it is and increment the count of that day depending on which one it is
            if word == 'gopal.ramasammycook@gmail.com':
                emails['gopal.ramasammycook@gmail.com'] += 1
            if word == 'louis@media.berkeley.edu':
                emails['louis@media.berkeley.edu'] += 1
            if word == 'cwen@iupui.edu':
                emails['cwen@iupui.edu'] += 1
            if word == 'antranig@caret.cam.ac.uk':
                emails['antranig@caret.cam.ac.uk'] += 1
            if word == 'rjlowe@iupui.edu':
                emails['rjlowe@iupui.edu'] += 1
            if word == 'gsilver@umich.edu':
                emails['gsilver@umich.edu'] += 1
            if word == 'david.horwitz@uct.ac.za':
                emails['david.horwitz@uct.ac.za'] += 1
            if word == 'wagnermr@iupui.edu':
                emails['wagnermr@iupui.edu'] += 1
            if word == 'zqian@umich.edu':
                emails['zqian@umich.edu'] += 1
            if word == 'stephen.marquard@uct.ac.za':
                emails['stephen.marquard@uct.ac.za'] += 1
            if word == 'ray@media.berkeley.edu':
                emails['ray@media.berkeley.edu'] += 1
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
all_emails = emails.keys()
store_words()
# print out the dictionary
print(emails)
