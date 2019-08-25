"""
Given a 32-bit signed integer, reverse digits of an integer.
Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        
        string_number = list(str(abs(x)))
        nubmer_len = len(string_number)
        for i in range(nubmer_len//2):
            string_number[i], string_number[nubmer_len-i-1] = string_number[nubmer_len-i-1], string_number[i] 
        
        number = int("".join(string_number))
        # Bad check for overflow
        if number < -2**31 or number > 2**31 - 1:
            return 0
        if(abs(x) == x):
            return number
        else:
            return -number
