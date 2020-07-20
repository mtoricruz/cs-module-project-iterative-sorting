# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # len(arr) - 1 bc once there's 1 item left in 
    # unsorted list, we don't have to run a comparison on it.
    #  Assume it's the highest value left

    # for every element in the length of the array
    for i in range(0, len(arr) - 1):
        # preserve current index variable for i
        cur_index = i
        # preserve smallest index variable in cur_index
        smallest_index = cur_index
        # each iteration we want the first element in the unsorted list
        # to be the default min
        
        # TO-DO: find next smallest element
        # for every element in the range i+1 (means to the right of the index) to the 
        # length of the array
        for elem in range(i+1, len(arr)):
            # if the elem positions value of the array is smaller than the current value of the smallest_index variable
            if arr[elem] < arr[smallest_index]:
                # replace the smallest index value with the current elem value
                smallest_index = elem

        # TO-DO: swap
        # Your code here
        # if smallest_index has a lower value than our default i, 
        if smallest_index != i:
            # then switch those items
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

        

    return arr


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):
#     # Your code here


#     return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
