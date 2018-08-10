#encoding:utf-8


"""
peak-index-in-a-mountain-array
Let's call an array A a mountain if the following properties hold:
A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
Input: [0,1,0]
Output: 1

Input: [0,2,1,0]
Output: 1

"""

import numpy as np
def peakIndexInMountainArray( A):

    """
    :type A: List[int]
    :rtype: int
    """
    #return np.argmax(A)
    return A.index(max(A))

if __name__ == '__main__':
    print(peakIndexInMountainArray([0,2,1,0]))