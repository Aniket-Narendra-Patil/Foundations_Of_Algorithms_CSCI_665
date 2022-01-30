"""
Filename: problem_5.2_Insertion_Sort.py

CSCI 665: Homework 1
Problem 5: Insertion Sort

Authors:
Aniket Narendra Patil
"""

# import statmenets are below

import random

"""
Insertion Sort:

Algorithm Analysis:

Basic Idea: Comapre key with values at previousIndex.

For n-1 iteration:

Do (In every iterations)

As long as previousIndex is greater than or equal to Zero 
AND
the value of key is less than the value at the previousIndex: 

Copy the value (larger value in this case) at previousIndex to location previousIndex + 1.
Decrement the previousIndex by 1.

Check for while loop condition again, and keep moving larger values by one position.

Once the loop reaches and index = 0 or or an index where key value is greater than
the previous value, copy the key value at that location

Repeat the above steps for n-1 iterations.

After completion of all (n-1) iterations, the input array will be sorted in ascending
order.

Time Complexity : O(n^2)

"""


# array of size n
def insertionSort(array):
    # Index position 1 to Index position (n-1)
    for index in range(1, len(array)):
        # Make the element at current index position as Key
        key = array[index]
        # Make the previousIndex value as (current index-1)
        previousIndex = index - 1

        # Checks if the key value is less than value at previousIndex (Index's) and based on results keeps moving
        # larger value one position to the right
        while previousIndex >= 0 and key < array[previousIndex]:
            array[previousIndex + 1] = array[previousIndex]
            previousIndex = previousIndex - 1

        # Finally, puts the small value at the appropriate location.
        array[previousIndex + 1] = key

    return array


# Test function for Insertion Sort

def testInsertionSort():

    # Uniform Distribution Test Case

    myUniformList = []
    inputVal1 = int(input('Enter the amount of numbers to be sorted: (Uniform Distribution) :'))
    for index1 in range(0, inputVal1):
        x = random.uniform(0, 1)
        myUniformList.append(x)
    print(insertionSort(myUniformList))

    # Gaussian Distribution Test Case

    myGausslList = []
    inputVal2 = int(input('Enter the amount of numbers to be sorted: (Gaussian Distribution) :'))
    for index1 in range(0, inputVal2):
        y = random.gauss(0.5, 0.0001)
        myGausslList.append(y)
    print(insertionSort(myGausslList))

    # Simple Test Case
    mySimpleList = [9, 3, 5, 7, 0, 2, 1, 4, 6, 8]
    print('Simple Test Case with Input list as :', mySimpleList)
    print(insertionSort(mySimpleList))


# Main conditional guard
if __name__ == '__main__':
    testInsertionSort()
