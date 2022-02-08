# declare an empty list for the words
words = []
# string for file name
file_name = "romeo.txt"


# define a function which reads the romeo.txt file line by line, and extracts the words from it, storing them in the
# list if they are not already in said list
def read_file():
    for line in open_file(file_name):
        for word in line.split():
            print(word)
            if word not in words:
                words.append(word)



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


print(read_file())
print(words)
