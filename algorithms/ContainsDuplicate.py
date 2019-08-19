class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for n in nums:
            if n in d:
                return True
            d[n] = True
        return False