#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the result
    result_list = []

    # Iterate through the elements in my_list
    for element in my_list:
        # If the current element matches the search element,
        # append the replacement element
        if element == search:
            result_list.append(replace)
        else:
            # Otherwise, append the current element as it is
            result_list.append(element)

    return result_list
