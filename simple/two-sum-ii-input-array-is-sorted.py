# encoding:utf-8

# 此方法效率较高
def twoSum(nums, target):
    s = set()
    for i in range(len(nums)):
        # 判断该数值是否曾经匹配过
        if nums[i] in s:
            continue
        tmp = target - nums[i]
        if nums[i + 1:].count(tmp) > 0:
            if i == nums.index(tmp):
                return [i, nums.index(tmp, i + 1)]
            else:
                return [i,nums.index(tmp)]
        # 未匹配上，加入集合
        s.add(nums[i])


if __name__ == '__main__':
    nums = [2, 4,  11, 15]
    print(twoSum(nums, 6))
