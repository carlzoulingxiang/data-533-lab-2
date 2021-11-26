class NumArrayTools:
    def __init__(self, arr):
        self.arr = arr

    def printArr(self):
        print(self.arr)

    def isnumerial(self):
        for i in self.arr:
            if not isinstance(i, int):
                return False
        return True

    def isnull(self):
        if len(self.arr) == 0:
            return True
        else:
            return False
    
    def appendArr(self, x):
        if isinstance(x, int):
            self.arr.append(x)
        else:
            print("Please append a number")