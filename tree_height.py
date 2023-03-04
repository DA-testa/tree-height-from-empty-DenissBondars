# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    # Your code here
    max_height = 0
    height_storage = n * [0]

    for i in range(n):
        if height_storage[i] == 0:
            current_height = 1
            edge = i
            while parents[edge] != -1:
                edge = parents[edge]
                if height_storage[edge] == 0:
                    current_height = current_height + 1
                else:
                    current_height = current_height + height_storage[edge]
                    break
            height_storage[i] = current_height
        else:
            current_height = height_storage[i]
        if current_height > max_height:
            max_height = current_height
    return max_height


def main():
    # implement input form keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    n = 0
    parents = 0
    FI = input()
    if "I" in FI:
        n = int(input())
        parents = input()
        parents = parents.split()
        parents = [int(i) for i in parents]
    if "F" in FI:
        test = input()
        test_file = "test/" + test
        if "a" in test:
            return
        else:
            with open(test_file) as file:
                n = int(file.readline())
                parents = file.readline().split()
                parents = [int(i) for i in parents]
    result = compute_height(n, parents)
    print(result)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))
