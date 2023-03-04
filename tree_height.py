# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    roots = np.argwhere(parents == -1).item()
    sort_out = np.array([roots])
    keep_track_head = 0
    keep_track_back = 1

    tested_elements = np.empty(n, dtype=bool)
    count_height = np.empty(n, dtype=int)
    
    tested_elements[roots] = True
    count_height[roots] = 1

    while keep_track_head < keep_track_back:
        current_element = sort_out[keep_track_head]
        keep_track_head = keep_track_head + 1
        descendants = np.flatnonzero(parents == current_element)
        for i in descendants:
            tested_elements[i] = True
            count_height[i] = count_height[i] + 1
            sort_out = np.append(sort_out, i)
            keep_track_back = keep_track_back + 1
        
    max_height = np.max(count_height)

    return max_height


def main():
    # implement input form keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    FI = input()
    if "I" in FI:
        n = int(input())
        parents = input()
        parents = np.array(parents.split(), dtype = int)
    if "F" in FI:
        test_file = input()
        if "a" in test_file:
            return
        else:
            with open(test_file, 'r') as f:
                n = int(f.readline())
                parents = f.readline()
                parents = np.array(parents.split(), dtype = int)
    result = compute_height(n, parents)
    print(result)
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
