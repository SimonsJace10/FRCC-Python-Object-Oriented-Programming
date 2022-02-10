# declare the file_name as words.txt
file_name = "../files/words.txt"
# instantiate words as an empty dictionary
words = {}


# function to store the words from the file in a dictionary
def store_words ():
    for line in open_file(file_name):
        for word in line.split():
            words[word] = None


# function to check whether a word is in the dictionary
def search (string):
    if string in words:
        return True
    else:
        return False


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
word_to_search_for = "word"
print(search(word_to_search_for))
