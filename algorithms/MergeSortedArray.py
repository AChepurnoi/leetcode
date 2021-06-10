from typing import List



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2):
            return
        
        nums2_idx = 0
        nums1_idx = 0
        carry = None
        while nums2_idx < len(nums2) and nums1_idx < m:
            if nums2[nums2_idx] < nums1[nums1_idx]:
                


a = [0,1,2,8,0,0]
b = [0,2]

Solution().merge(a, 4, b, 2)
print(a)
