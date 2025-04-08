class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            x = nums[i]
            for j in range(len(nums)):
                y = nums[j]
                if (x + y == target) and (i != j):
                    return [i,j]
                    break

        