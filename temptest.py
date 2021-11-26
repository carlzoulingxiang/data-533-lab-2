from arraytools.chararraytools import CharArraySearchTool as cast
from arraytools.chararraytools import CharArraySortTool as casort
from arraytools.numarraytools import NumArraySearchTool as numst
from arraytools.numarraytools import NumArraySortTool as numsort

if __name__ == '__main__':
    myArr = ['e', 'a', 'd', 'c', 'b']
    charTool = cast.CharArraySearchTool(myArr)
    charTool.append('f')

    max = charTool.search_max()
    print(max)
    min = charTool.search_min()
    print(min)
    res = charTool.search_key('c')
    print(res)

    sortTool = casort.CharArraySortTool(myArr)
    sortTool.sort_asc()
    print(sortTool.arr)
    sortTool.sort_desc()
    print(sortTool.arr)
    sortTool.unsorting()
    print(sortTool.arr)

    sortTool.check_empty()

    print("----------------------Number Array tools----------------")

    arr = [2,3,6,1,9,4]
    numtool = numst.NumArraySearchTool(arr)
    numtool.append(10)
    print(numtool.arr)

    numMax = numtool.searchMax()
    print(numMax)
    numMin = numtool.searchMin()
    print(numMin)
    numRes = numtool.searchTarget(6)
    print(numRes)

    numSearch = numsort.NumArraySortTool(arr)
    numSearch.AscendingSort()
    print(numSearch.arr)
    numSearch.DescendingSort()
    print(numSearch.arr)
    numSearch.Unsort()
    print(numSearch.arr)

    numSearch.isnull()
