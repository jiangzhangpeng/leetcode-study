# encoding:utf-8
"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place.The move sequence is represented by a string. And each move is represent
by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false
representing whether the robot makes a circle.
Input: "UD"
Output: true

Input: "LL"
Output: false
"""


def judgeCircle1(moves):
    """
    :type moves: str
    :rtype: bool
    """
    origin = [0, 0]
    for t in moves:
        if t == 'L':
            origin[0] += 1
        elif t == 'R':
            origin[0] -= 1
        elif t == 'U':
            origin[1] += 1
        elif t == 'D':
            origin[1] -= 1

    if origin[0] == 0 and origin[1] == 0:
        return True
    else:
        return False


def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """

    if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
        return True
    else:
        return False


if __name__ == '__main__':
    print(judgeCircle('UD'))
