# encoding:utf-8

'''注意事项
1、末尾有0
2、负数
3、上溢、下溢
'''


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    s_min = str(2 ** 31)
    if x == 0:
        return 0
    if x < 0:
        sign = '-'
    else:
        sign = ''
    s = str(x).lstrip('-').rstrip('0')[::-1]
    if len(s) >= 10 and s > s_min:
        return 0
    else:
        return int(sign + s)

    print(s)


def reverse1(x):
    s = -1  # cmp(x, 0)
    r = int('s*x'[::-1])
    return s * r * (r < 2 ** 31)


def reverse2(x):
    if x == 0:
        return 0
    sign = 1
    if x < 0:
        sign = -1
    tmp = int(str(x * sign)[::-1])
    return tmp * sign * (tmp < 2 ** 31)


if __name__ == '__main__':
    x = -10  # -120#-123#1534236469
    print(reverse2(x))
