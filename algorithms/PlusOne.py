from typing import List

"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = digits[-1]
        last = last + 1
        digits[-1] = last
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] = digits[i-1] + 1
            else: 
                return digits
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits
            
        