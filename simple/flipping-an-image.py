# encoding:utf-8
'''
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
'''


# 利用矩阵变换
def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """

    from numpy import mat, zeros, eye, shape
    A = mat(A)
    sigma = zeros(shape=shape(A), dtype=int)
    for i in range(shape(A)[0]):
        sigma[i][(shape(A)[0] - 1 - i)] = 1
    A = A * sigma
    sigma = eye(shape(A)[0], dtype=int) * -1
    A = (A - 1) * sigma
    return A.tolist()

def flipAndInvertImage1(A):
    for row in A:
        for i in range(int((len(row) + 1) / 2)):
            row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
    return A
if __name__ == '__main__':
    A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    #print(flipAndInvertImage1(A))

    b = [1,2,3,4,5]
    print(b[1])
    print(b[~1])
