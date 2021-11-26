from arraytools.chararraytools import CharArraySearchTool as cast
from arraytools.chararraytools import CharArraySortTool as casort

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







