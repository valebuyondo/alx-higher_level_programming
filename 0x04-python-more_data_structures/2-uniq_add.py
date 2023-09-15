#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()

    # Initialize a variable to store the sum
    sum_unique = 0

    # Iterate through the elements in my_list
    for element in my_list:
        # Check if the element is an integer and not already in the unique_integers set
        if isinstance(element, int) and element not in unique_integers:
            # Add the unique integer to the set and add it to the sum
            unique_integers.add(element)
            sum_unique += element

    return sum_unique

