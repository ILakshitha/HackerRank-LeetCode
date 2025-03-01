class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2

        x = sorted(nums3)

        print(len(x))
        mid = len(x)//2
        if len(x)%2 == 0:
            return (x[mid] + x[mid-1])/2.0
        else:

            return x[mid]