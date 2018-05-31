# encoding:utf-8
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

#不能使用set ，存在[1,1,1]这种数据
#方法1、2、3逐步优化

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum1(nums, target):
    l_ss = sorted(nums)
    for i in range(len(l_ss)):
        for j in range(i + 1, len(l_ss)):
            if l_ss[i] + l_ss[j] == target:
                ind0 = nums.index(l_ss[i])
                ind1 = nums.index(l_ss[j])

                if ind0 < ind1:
                    return [ind0, ind1]
                elif ind0 > ind1:
                    return [ind1, ind0]
                else:
                    return [ind0, nums.index(l_ss[j], (ind0 + 1))]
            if l_ss[i] + l_ss[j] > target:
                break



def twoSum2(nums, target):
    l_ss = sorted(nums)
    s = set()
    for i in range(len(l_ss)):
        #判断该数值是否曾经匹配过
        if l_ss[i] in s:
            continue
        for j in range(i + 1, len(l_ss)):
            if l_ss[i] + l_ss[j] == target:
                ind0 = nums.index(l_ss[i])
                ind1 = nums.index(l_ss[j])

                if ind0 < ind1:
                    return [ind0, ind1]
                elif ind0 > ind1:
                    return [ind1, ind0]
                else:
                    return [ind0, nums.index(l_ss[j], (ind0 + 1))]
            if l_ss[i] + l_ss[j] > target:
                break
        #未匹配上，加入集合
        s.add(l_ss[i])

#此方法效率较高
def twoSum3(nums, target):
    l_ss = sorted(nums)
    s = set()
    for i in range(len(l_ss)):
        #判断该数值是否曾经匹配过
        if l_ss[i] in s:
            continue
        tmp = target - l_ss[i]
        if l_ss.count(tmp) > 0:
            ind0 = nums.index(l_ss[i])
            ind1 = nums.index(tmp)
            if ind0 < ind1:
                return [ind0, ind1]
            elif ind0 > ind1:
                return [ind1, ind0]
            else:
                return [ind0, nums.index(tmp, (ind0 + 1))]
        #未匹配上，加入集合
        s.add(l_ss[i])

if __name__ == '__main__':
    nums = [4, 4, 11, 15]
    print(twoSum3(nums,8))
