# encoding:utf-8

"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are
overlapped while the others are not.You need to merge them into a new binary tree. The merge rule is that if two
nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used
as the node of new tree.
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
"""


def mergeTrees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    merged = []
    k = min(len(t1), len(t2))
    for i in range(0, k):
        if t1[i] == 'null' and t2[i] == 'null':
            merged.append( 'null')
            continue
        if t1[i] != 'null' and t2[i] == 'null':
            merged.append(t1[i])
            continue
        if t2[i] != 'null' and t1[i] == 'null':
            merged.append(t2[i])
            continue
        merged.append(t1[i] + t2[i])
    if len(t1) > k:
        merged.extend(t1[k:])
    if len(t2) > k:
        merged.extend(t2[k:])
    return merged


if __name__ == '__main__':
    print(mergeTrees([1, 3, 2, 5], [2, 1, 3, 'null', 4, 'null', 7]))
