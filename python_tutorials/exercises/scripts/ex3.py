# Write a binary function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

# Binary search works looking at the middle element of the list and takes the left or right half
# if the item is less or greater then the middle element. The procedure is then repeated until the element is
# found.

# Hint: import math for the floor, ceil functions

##############################################
#                  SOLUTION
##############################################

import math


def bin_search(item, li):
    """
    Binary search algorithm
    :param item:   item to be searched
    :param li:     list to search in
    :return:       the index where the item is stored
    """
    # Check if item can be in the list
    if item < li[0] or item > li[-1]:
        print("Item not in the list.")
        return

    top = len(li)
    bottom = 0

    while bottom != top:
        half_idx = math.floor((top + bottom)/2)
        if item > li[half_idx]:
            bottom = half_idx + 1
        elif item < li[half_idx]:
            top = half_idx
        else:
            print("Item stored at index", half_idx)
            return half_idx

    print("Item not in the list")
    return -1


my_list = [1, 4, 6, 7, 9, 12, 15, 18, 19, 20]

bin_search(4, my_list)
bin_search(19, my_list)
bin_search(16, my_list)
bin_search(22, my_list)
bin_search(1, my_list)
bin_search(20, my_list)

