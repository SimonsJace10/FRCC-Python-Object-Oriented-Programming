# example list
my_list = ['A', 'B', '1', 'Hello', 'Jace', 'Mr. Gilanyi']


# define chop function which modifies the list by removing its first and last elements
def chop(chop_list):
    chop_list.pop(0)
    chop_list.pop(len(chop_list)-1)
    return None


# define middle function which takes
def middle(input_list):
    new_list = input_list
    chop(new_list)
    return new_list


print("Original list: " + str(my_list))
print("Chopped list: " + str(middle(my_list)))
