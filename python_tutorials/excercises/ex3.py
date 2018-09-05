# Write a binary function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

# Binary search works looking at the middle element of the list and takes the left or right half
# if the item is less or greater then the middle element. The procedure is then repeated until the element is
# found.

# Hint: import math for the floor, ceil functions

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

    while True:
        half_idx = math.floor(len(li)/2)
        if item > li[half_idx]:
            li = li[half_idx:]
        elif item < li[half_idx]:
            li = li[:half_idx]
        else:
            print("Item stored at index", half_idx, ".")
            return half_idx

        if len(li) == 1:
            print("Item not in the list.")


my_list = [1, 4, 6, 7, 9, 12, 15, 18, 19, 20]

bin_search(4, my_list)
#bin_search(my_list, 19)
#bin_search(my_list, 16)
