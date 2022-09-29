"""
从数组中找两个索引
是target 的和的索引
"""


class Solution(object):
    @staticmethod
    def sum(nums, target=9):
        n = len(nums)
        for x in range(n):
            for y in range(x+1, n):
                if nums[x] + nums[y] == target:
                    print(x, y)
                    break


num = [11, 2, 15, 7]
Solution.sum(num)



