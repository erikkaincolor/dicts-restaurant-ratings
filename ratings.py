"""Restaurant rating lister."""

# Your job is to write a program named ratings.py that:
#     Reads the ratings in from the file
#     Stores them in a dictionary
#     And finally, spits out the ratings in alphabetical order by restaurant

# Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.
# Hint 2: Refer to the Python docs on the sorted() function if you need a reminder of how to sort.

def get_new_profile(new_profile):
    """takes in dictionary, adds key:value pair based on user input"""

    new_rest = input("Restaurant name here: ")
    new_rating = input("Rating here: ")
    new_profile[new_rest] = new_rating


def display_sorted_restaurants(unsorted_restaurant_dict):
    """creates sorted list from unsorted dictionary 
       and outputs dictionary values using sorted list items as keys"""
    
    sorted_restaurant_dict_list = sorted(unsorted_restaurant_dict)
    for restaurant in sorted_restaurant_dict_list:
        print(f"{restaurant} is rated at {unsorted_restaurant_dict[restaurant]}.")


def alpha_ratings(input_file):
    """read rating from file, print them in order of restaurant"""

    file = open(input_file)
    new_dict = {}
    # strip space on right side of end of line via .rstrip()
    for line in file: # for loop:
        line = line.rstrip() # iterate through file line by line and SPLIT string into two strings, delimiter (":")
        restaurant = line.split(":") #returns a list
        new_dict[restaurant[0]] = restaurant[1]
        
    display_sorted_restaurants(new_dict)
    get_new_profile(new_dict)
    display_sorted_restaurants(new_dict)

        
alpha_ratings("scores.txt")

""""""I could not run program to test or debug as the terminal is running super slow
    and it's only showing one line of text at a time, I think it's a live share thing. I think this should work though. """