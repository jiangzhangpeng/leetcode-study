# encoding:utf-8
"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Input: "Hello"
Output: "hello"

Input: "here"
Output: "here"

Input: "LOVELY"
Output: "lovely"
"""

def toLowerCase(str):
    """
    :type str: str
    :rtype: str
    """
    return str.lower()


if __name__ == '__main__':
    print(toLowerCase('AAA'))