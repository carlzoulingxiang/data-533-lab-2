from arraytools.numarraytools.NumArrayTools import NumArrayTools
class NumArraySearchTool(NumArrayTools):
    def __init__(self, arr):
        NumArrayTools.__init__(self,arr)
        if (self.isnumerial() != True) or (self.isnull() != False):
            print("please enter a valid array")
            
    def searchMin(self):
        return min(self.arr)
    
    def searchMax(self):
        return max(self.arr)
    
    def searchTarget(self,target):
        for i in range(len(self.arr)):
            if target == self.arr[i]:
                return i
        return "Not found"
    