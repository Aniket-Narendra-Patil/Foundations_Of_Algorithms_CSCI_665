"""
Filename: problem_5.3_Bucket_Sort.py

CSCI 665: Homework 1
Problem 5: Bucket Sort

Authors:
Aniket Narendra Patil
"""

# import statmenets are below

import math
import random

"""
Bucket Sort:

Algorithm Analysis:

Basic Idea: Divide the input (uniformly distributed) values into array of size of input
where each input array location is a linked list.

Each array location can be called as a bucket which holds data in a particular range,
say for input values in range [0, 1) and 8 input values,
there will be 8 locations in the array where,
index_0 holds data in range 0 - 0.125
index_1 holds data in range 0.125 - 0.250 and so on. 

Time Complexity : Expected Run time: O(n)

Since the input elements n are uniformly distributed, as per mathametical analysis, the input will be distibuted 
even in the given range [0, k). There we will roughly have equal number of input values in
each bucket, where we have created n buckets for n input values. 
So for truely uniform data, we will get roughly one input value in each bucket we created.

Now, independent of the sorting algorithm we use, we are guaranted we will have a constant number of
input value(s) in each bucket which can be sorted in constant time.

Best Case: O(n)
Each linked list takes ends up with a single element and insertion sort takes constant time per list.
Total cost of insertion sort is Theta(n)

Worst Case: O(n^2)
All elements end up in a singe list and insertion sort takes O(n^2) to sort all elements.

"""


def bucketSort(inputList):
    # length = length of the input array
    length = len(inputList)
    # auxiliary array of length same as input array where each array index is a linked list
    auxArray = []

    # allocate aux array of size 'length' and initalize every index location of array as an empty linked list.
    for index in range(length):
        auxArray.append([])

    # calculate the location where the data in the array will be copied to based on the formula
    # Floor ( length_of_input_array * data )
    for index2 in range(0, length):
        auxArray[math.floor(length * inputList[index2])].append(inputList[index2])
        # Using append operation ensures that the sorting is stable.
        # If the linked list at a specified location is empty, then the append operation works actually as a prepend operation and
        # adds the element at the first available position of the linked list.

    # run insertion sort on each individual linked list and store the sorted list in the same location
    for index3 in range(length):
        auxArray[index3] = insertionSort(auxArray[index3])

    # copy each sorted linked list to the respective inputList location
    k = 0
    for i in range(length):
        for j in range(len(auxArray[i])):
            # copying sorted linked list at location [i] element by element [j] into inputList[k]
            inputList[k] = auxArray[i][j]
            # increment inputList index k by 1
            k += 1
    # returns the sorted inputList
    return inputList


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


def testBucketSort():
    # Uniform

    myUniformList = []
    inputVal1 = int(input('Enter the amount of numbers to be sorted: (Uniform Distribution) :'))
    for index1 in range(0, inputVal1):
        x = random.uniform(0, 1)
        myUniformList.append(x)
    print(bucketSort(myUniformList))

    # Gaussian Distribution Test Case

    myGausslList = []
    inputVal2 = int(input('Enter the amount of numbers to be sorted: (Gaussian Distribution) :'))
    for index1 in range(0, inputVal2):
        y = random.gauss(0.5, 0.0001)
        myGausslList.append(y)
    print(bucketSort(myGausslList))

    # Simple Test Case

    mySimpleList = [0.5, 0.8, 0.1, 0.6, 0.3, 0.32, 0.55, 0.79, 0.87]
    print('Simple Test Case with Input list as:', mySimpleList)
    print(bucketSort(mySimpleList))


if __name__ == '__main__':
    testBucketSort()
