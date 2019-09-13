
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        current_index = 0
        if len(strs) == 0:
            return ""
        while True:
            if len(strs[0]) <= current_index:
                break
            first = strs[0][current_index]
            stop, not_equal = False, False
            for s in strs:
                if len(s) <= current_index:
                    stop = True
                    break

                if s[current_index] != first:
                    not_equal = True
                
            if stop or not_equal: 
                break
            current_index += 1
        
        return strs[0][:current_index]
