"""
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity
must be in the order of O(log n).
"""


def rotated_array_search(arr, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       arr(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if not arr:
        return -1

    if len(arr) == 1:
        if arr[0] == number:
            return 0
        else:
            return -1
        
    # If array is not rotated
    if arr[0] < arr[-1]:
        return binary_search(arr, number, 0, len(arr) - 1)

    pivot = find_pivot(arr, 0, len(arr) - 1)

    # look left
    result = binary_search(arr, number, 0, pivot)

    if result != -1:
        return result

    # look right
    return binary_search(arr, number, pivot, len(arr) - 1)


def binary_search(arr, number, left, right):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == number:
            return mid

        if arr[mid] > number:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def find_pivot(arr, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid - 1] > arr[mid]:
        return mid

    if arr[mid] < arr[mid - 1]:
        return mid - 1

    if arr[left] > arr[mid]:
        return find_pivot(arr, left, mid + 1)
    else:
        return find_pivot(arr, mid, right)


def linear_search(arr, number):
    for index, element in enumerate(arr):
        if element == number:
            return index
    return -1


def test_function(test_case):
    arr = test_case[0]
    number = test_case[1]
    if linear_search(arr, number) == rotated_array_search(arr, number):
        print("Pass")
    else:
        print("Fail")


# Edge cases

# Empty list
arr = []
print(rotated_array_search(arr, 22))
# -1

print('------------------------------')

# Large values
arr = [354359, 9546444, 454656, 58974, 856497, 67845]
print(rotated_array_search(arr, 58974))
# print 1

print('------------------------------')

# Number not found
arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
print(rotated_array_search(arr, 54654416))
# -1
print('-----------------------------')

# array not rotated
arr = [1, 2, 3]
print(rotated_array_search(arr, 3))
# 2
print('------------------------------')

# One value
arr = [3]
print(rotated_array_search(arr, 3))
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
