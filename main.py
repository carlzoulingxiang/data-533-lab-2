"""
This is Sample Test Code For arraytools Package

@Author: Nelson Tang, Ling Xiang Zou
@Date: Nov 25, 2021
"""

from arraytools.chararraytools import CharArraySearchTool as csearch
from arraytools.chararraytools import CharArraySortTool as csort


if __name__ == '__main__':

    """
    The following are sample test to demonstrating how to use the chararraytools package
    """
    charArr = ['e', 'a', 'd', 'c', 'b']
    # create an object of CharArraySortTool
    charSortTool = csort.CharArraySortTool(charArr)
    charSearchTool = csearch.CharArraySearchTool(charArr)

    # check all element in this array are char
    if charSortTool.__instancecheck__():
        print("All elements in the array are character!")
    else:
        print("Character Sort Tool containing an non-char element!")

    if charSearchTool.__instancecheck__():
        print("All elements in the array are character!")
    else:
        print("Character Search Tool containing an non-char element!")

    # check whether is an empty array
    if charSortTool.check_empty():
        print("Character Sort Tool containing an empty array!")
    else:
        print("Character Sort Tool containing an non-empty array!")

    if charSearchTool.check_empty():
        print("Character Search Tool containing an empty array!")
    else:
        print("Character Search Tool containing an non-empty array!")

    # append an new element into array
    charSortTool.append('f')
    charSearchTool.append('t')

    # print the array
    print("Sort tool array: ", charSortTool)
    print("Search tool array: ", charSearchTool)

    # find the max char in array
    maxNum = charSearchTool.search_max()
    print("The max character in this array is: ", maxNum)

    # find the min char in array
    minNum = charSearchTool.search_min()
    print("The min character in this array is: ", minNum)

    # search an target in array
    res = charSearchTool.search_key('c')
    if res == -1:
        print("Target not found!")
    else:
        print("The index of target in this array is: ", res)

    # check array is sorted
    if charSortTool.sorted:
        print("Array is sorted!")
    else:
        print("Array is unsorted!")

    # sort array in ascending alphabetical order
    charSortTool.sort_asc()
    print("The ascending sorted array is: ", charSortTool)

    # sort array in descending alphabetical order
    charSortTool.sort_desc()
    print("The descending sorted array is: ", charSortTool)

    # unsort this array
    charSortTool.unsort()
    print("The unsorted array is: ", charSortTool)

"""
The following are the outputs of the above test code:

All elements in the array are character!
All elements in the array are character!
Character Sort Tool containing an non-empty array!
Character Search Tool containing an non-empty array!
Sort tool array:  ['e', 'a', 'd', 'c', 'b', 'f', 't']
Search tool array:  ['e', 'a', 'd', 'c', 'b', 'f', 't']
The max character in this array is:  t
The min character in this array is:  a
The index of target in this array is:  3
Array is unsorted!
The ascending sorted array is:  ['a', 'b', 'c', 'd', 'e', 'f', 't']
The descending sorted array is:  ['t', 'f', 'e', 'd', 'c', 'b', 'a']
The unsorted array is:  ['e', 't', 'f', 'a', 'd', 'b', 'c']
"""





