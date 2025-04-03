class Solution(object):
    def findDifference(self, nums1, nums2):
        set1, set2 = set(nums1), set(nums2)
        difference_1 = sorted(set1 - set2)
        difference_2 = sorted(set2 - set1)
        answer = [list(difference_1),list(difference_2)]
        return answer

        