# encoding:utf-8

def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    num = 0
    for k in set(J):
        num += S.count(k)
    return num


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(J,S))
