# declare the file_name as words.txt
file_name = "../files/mbox-short.txt"
# instantiate dictionary with hours and starting at count 0
hours = {'04': 0, '06': 0, '07': 0, '09': 0, '10': 0, '11': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0}


def extract_hours():

    # for every line ...
    for line in open_file(file_name):
        # ... if the line starts with 'From ' ...
        if line.startswith("From "):
            temp_list = line.split()
            # the timestamp is always the 5th item in the split list
            timestamp = temp_list[5]
            # split the timestamp at :
            hour = timestamp.split(':')
            # set the dictionary item corresponding to the hour at index 0 in the timestamp list to its count + 1
            hours[hour[0]] += 1
        else:
            continue


# hour frequency finally prints out the totals for each hour
def hour_frequency():
    for item in hours:
        print(item + ': ' + str(hours[item]))


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
extract_hours()
# print out the list
hour_frequency()
