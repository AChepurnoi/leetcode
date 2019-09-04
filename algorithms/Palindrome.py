class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        left_index = 0
        right_index = len(s) - 1
        
        while left_index < right_index:
            l = s[left_index]
            r = s[right_index]
            if l.isalnum() and r.isalnum():
                if l.lower() != r.lower():
                    return False
                else:
                    left_index +=1
                    right_index -=1
            elif not l.isalnum():
                left_index +=1
            elif not r.isalnum():
                right_index -= 1
            
        return True

            
