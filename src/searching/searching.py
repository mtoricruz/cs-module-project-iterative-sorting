# def linear_search(arr, target):
#     # Your code here
#     i = 0 # counter for loop

#     # loop through array
#     while i < len(arr):
#         if arr[i] == target:
#             return 
#         i = i + 1 # this increments the i value to move through the array
        
#     return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # since we want to find middle position of each iteration
    # we need to know the beginning/ending position
    begin_index = 0
    end_index = len(arr) - 1
 
    while begin_index <= end_index:
        # the midpoint should be between our beg index and the rest of the items in our arr
        midpoint = begin_index + (end_index - begin_index) // 2
        # this will return the index VALUE, instead of the index POSITION
        midpoint_value = arr[midpoint]
        # if the midpoint value is the target value
        if midpoint_value == target:
            # return the midpoint
            return midpoint
        # if the target value is less than the midpoint value,
        elif target < midpoint_value:
            # the target is to the left of the midpoint value
            # change our ending position 
            # the ending position is now to the left of the old midpoint
            end_index = midpoint - 1
        # if the target value is greater than midpoint value,
        else:
            # the target is to the right of the midpoint value
            # change our starting position
            # the beginning index position is now to the right of the old midpoint
            begin_index = midpoint + 1

    return -1  # not found
