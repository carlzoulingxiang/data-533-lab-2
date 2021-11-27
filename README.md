# Data533 Lab 2
- Students: Ling Xiang Zou (60038213), Tang Ao (64277791)
- Date: Nov 26, 2021

In this lab, we aim to create a package called arraytools for searching and sorting arrays of characters and numbers.

The following are the structure and the function details of arraytools:

# Data533 Lab 2
- Students: Ling Xiang Zou (60038213), Tang Ao (64277791)
- Date: Nov 26, 2021

In this lab, we aim to create a package called arraytools for searching and sorting arrays of characters and numbers.

The following are the structure and the function details of arraytools:

- **arraytools**
  - **chararraytools**: Handle character arrays
    - **CharArrayTools.py**
    - Containing CharArrayTools class.
      - **\_\_init\_\_**: Set an array attribute of class.
      - **\_\_str\_\_**: Convert CharArrayTools to string for print.
      - **\_\_instancecheck\_\_**: Check each element in this array is character.
      - **check_empty()**: Check whether the array is empty.
      - **append(element)**: Insert an element into the array.
    - **CharArraySortTool.py**
    - Containing CharArraySortTool class that inherits CharArrayTools class.
      - **\_\_init\_\_**: Set an array and a sorted(boolean) attribute of class 
      - **sort_asc()**: Sort the character array in ascending alphabetical order by implementing a bubble sort.
      - **sort_desc()**: Sort the character array in descending alphabetical order.
      - **unsort()**: Make a sorted array to unsorted.
    - **CharArraySearchTool.py**
    - Containing CharArraySearchTool class that inherits CharArrayTools class.
      - **\_\_init\_\_**: Set an array attribute of class.
      - **search_min()**: Search the minimum element in the array.
      - **search_max()**: Search the maximum element in the array.
      - **search_key(target)**: Search a character in the array by implementing a linear search

  - **numarraytools**: Handle integer arrays
    - **NumArrayTools.py**
    - Containing numArrayTools class.
      - **\_\_init\_\_**: Set an array attribute of class.
      - **isnumerial()**: Check each element in this array is integer.
      - **isnull()**: Check whether the array is empty.
      - **append(element)**: Insert an element into the array.
    - **NumArraySortTool.py**
    - Containing NumArraySortTool class that inherits NumArrayTools class.
      - **\_\_init\_\_**: Set an array and verify that the array is not empty and the elements are all integers 
      - **AscendingSort()**: Sort the number array in ascending order 
      - **DescendingSort()**: Sort the number array in descending order
      - **Unsort()**: Make a sorted array to unsorted.
    - **NumArraySearchTool.py**
    - Containing NumArraySearchTool class that inherits NumArrayTools class.
      - **\_\_init\_\_**: Set an array and verify that the array is not empty and the elements are all integers.
      - **searchMin()**: Search the minimum number in the array.
      - **searchMax()**: Search the maximum number in the array.
      - **searchTarget(target)**: Search a target number in the array by implementing a linear search