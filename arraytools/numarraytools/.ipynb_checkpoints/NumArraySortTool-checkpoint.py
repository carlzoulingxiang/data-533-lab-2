import random
from arraytools.numarraytools.NumArrayTools import NumArrayTools
class NumArraySortTool(NumArrayTools):
    def __init__(self, arr):
        NumArrayTools.__init__(self,arr)
        if (self.isnumerial() != True) or (self.isnull() != False):
            print("please enter a valid array")
    

    def AscendingSort(self):
        self.arr.sort()
        self.printArr()

    
    def DescendingSort(self):
        self.arr.sort(reverse=True)
        self.printArr()
    
    def Unsort(self):
        self.arr = random.sample(self.arr,len(self.arr))
        self.printArr()