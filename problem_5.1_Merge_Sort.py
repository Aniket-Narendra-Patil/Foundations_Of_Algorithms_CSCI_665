"""
Filename: problem_5.1_Merge_Sort.py

CSCI 665: Homework 1
Problem 5: Merge Sort

Authors:
Aniket Narendra Patil
"""

# import statmenets are below

import random

"""
Merge Sort:

Algorithm Analysis:

Basic Idea: Recursively splits the input list into two halves and goes on splitting until the all the newly generated lists are sorted.
Follows a Divide and Conquer approch.

Divide: Divides the list until its sorted (has only one element).
Conquer: Combine all sorted lists together to form a single sorted list.

Base Case: A list is considered to be sorted if the length of the list is equal to 1.
Recursive Case: The list consists more than one element.

Once the two halves are sorted, we perform the merge step. Merge step combines the two sorted lists into one sorted list.

Time Complexity Analysis:

Time Complexity : O(n * log n)

T(n) = 
MergeSort(X, n):
Base Condition if n(length of array A) == 1, then return X (Sorted Array) - O(1)
Calculate the middleIndex = len(A) // 2 using formula - O(1)
Use the middleIndex to split the array into two halves 
A = X[0: middle - 1] - O(n)
B = X[middle: n] - O(n)
As = MergeSort[A, middle] - T(n/2)
Bs = MergeSort[B, n- middle] - T(n/2)
return Merge(As, Bs) - O(n)

T(n) = O(n) + 2 * T(n/2)
T(n) = O(n * log n)

"""


def mergeSort(aList: list):
    """
    The recursive mergeSort function that splits the list into two halves recurrsively until all the newly generated lists are sorted (length == 1),
    and then merges all sorted lists to form a single sorted list.
    :param aList: Single unsorted list
    :return: Single sorted list
    """

    # Base Condition
    if len(aList) == 1:
        return aList

    # Recursive Condition

    # Calculate middle index to split list into two halves
    midIndex = len(aList) // 2

    # Recursively splits the list until, each new generated list is sorted
    first = mergeSort(aList[0:midIndex])
    second = mergeSort(aList[midIndex:len(aList)])

    # to store the final sorted array
    ans = []
    firstIndex = 0
    secondIndex = 0

    # while there are still elements to compare in the first list and while there are still elements to compare in the second list
    while firstIndex < len(first) and secondIndex < len(second):
        # if element in first list is smaller than element in the second list
        if first[firstIndex] < second[secondIndex]:
            # add that element in the first list
            ans.append(first[firstIndex])
            # increment the index of the first list
            firstIndex += 1

        else:
            # if element in first list is not smaller than element in the second list
            # add the element in the second list
            ans.append(second[secondIndex])
            # increment the index of the second list
            secondIndex += 1

    # adds remainder of the other list
    if firstIndex < len(first):
        # if index of first list is less than length of the first list
        # adds the remainder of the first list to the answer
        ans.extend(first[firstIndex:])

    else:
        # adds remainder of the second list to the answer
        ans.extend(second[secondIndex:])

    # returns the entire sorted list
    return ans


def testMergeSort():
    
    # Uniform Distribution Test Case

    myUniformList = []
    inputVal1 = int(input('Enter the amount of numbers to be sorted: (Uniform Distribution) :'))
    for index1 in range(0, inputVal1):
        x = random.uniform(0, 1)
        myUniformList.append(x)
    print(mergeSort(myUniformList))

    # Gaussian Distribution Test Case

    myGausslList = []
    inputVal2 = int(input('Enter the amount of numbers to be sorted: (Gaussian Distribution) :'))
    for index1 in range(0, inputVal2):
        y = random.gauss(0.5, 0.0001)
        myGausslList.append(y)
    print(mergeSort(myGausslList))

    # Simple Test Case
    mySimpleList = [9, 3, 5, 7, 0, 2, 1, 4, 6, 8]
    print('Simple Test Case with Input list as :', mySimpleList)
    print(mergeSort(mySimpleList))


if __name__ == '__main__':
    testMergeSort()
