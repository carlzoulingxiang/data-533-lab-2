"""
Character Array searching tool

@Author: Nelson Tang
@Date: Nov 25, 2021
"""
from arraytools.chararraytools.CharArrayTools import CharArrayTools


class CharArraySearchTool(CharArrayTools):
    def __init__(self, arr):
        CharArrayTools.__init__(self, arr)

    def search_min(self):
        return min(self.arr)

    def search_max(self):
        return max(self.arr)

    def search_key(self, key):
        """
        Search a character in the array by implementing a binary search
        :param key: a character
        :return: The index of the target, if not found return -1.
        """

        left = 0
        right = len(self.arr)
        while left <= right:
            mid = left + ((right - left) // 2)
            res = (key == self.arr[mid])
            if res == 0:
                return mid - 1
            if res > 0:
                left = mid + 1
            else:
                right = mid - 1
        return -1


