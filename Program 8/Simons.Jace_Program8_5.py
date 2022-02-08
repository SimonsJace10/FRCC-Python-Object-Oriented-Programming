# instantiate file_name to the mbox short file
file_name = "../Files/mbox-short.txt"
count = 0

def parse_file(count):
    for line in open_file(file_name):
        if line.startswith("From"):
            count += 1
            words = line.split()
            print(words[1])
    return "There were " + str(count) + " lines that started with 'From'"


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


print(parse_file(count))
