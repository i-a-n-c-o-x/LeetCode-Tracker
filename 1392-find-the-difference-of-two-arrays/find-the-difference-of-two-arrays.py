class Solution(object):
    def findDifference(self, nums1, nums2):
        set1, set2 = set(nums1), set(nums2)
        answer = [list(sorted(set1-set2)),list(sorted(set2-set1))]
        return answer

        