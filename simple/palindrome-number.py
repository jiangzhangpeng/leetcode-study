# encoding:utf-8
'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''


def isPalindrome(x):
    if (x > 0 and x % 10 == 0) or x < 0:
        return False
    p, k = x, 0
    while p > 0:
        k = k * 10 + p % 10
        p = p // 10
    if k == x:
        return True
    else:
        return False


def isPalindrome1(x):
    if (x > 0 and x % 10 == 0) or x < 0:
        return False
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False


# 参考solution  只计算一半，比最初的方法减少一半计算量
def isPalindrome2(x):
    if (x > 0 and x % 10 == 0) or x < 0:
        return False
    rx = 0
    while x > rx:
        rx = rx * 10 + x % 10
        x = x // 10
    return rx == x or rx // 10 == x


if __name__ == '__main__':
    x = 1002001
    print(isPalindrome2(x))
