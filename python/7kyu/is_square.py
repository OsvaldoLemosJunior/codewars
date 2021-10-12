"""
Are they square?

Write a function that checks whether all elements in an array are square numbers. The function should be able to take any number of array elements.

Your function should return true if all elements in the array are square numbers and false if not.

An empty array should return undefined / None / nil /false (for C). You can assume that all array elements will be positive integers.

Examples:

is_square([1, 4, 9, 16]) --> True

is_square([3, 4, 7, 9]) --> False

is_square([]) --> None
"""
def is_square(arr):
    
    # if array is empty return None
    if arr:
        #for each number inside array
        for num in arr:
            # fisrt calculation sqrt and then apply power 2 if number (int) 
            # is different as input return False
            if num != int(num**0.5)**2:
                return False
        # if not returned yet, means that all numbers are perfect squares
        return True
    else:
        return None


print(is_square([74, 74, 70, 62,85,41, 7]))