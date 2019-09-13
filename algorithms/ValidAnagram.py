class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        appearences = {}
        for letter in s:
            count = appearences.get(letter, 0) + 1
            appearences[letter] = count

        for letter in t:
            count = appearences.get(letter, 0)
            if count == 0:
                return False
            elif count == 1:
                del appearences[letter]
            else:
                count -=1
                appearences[letter] = count
            
        return len(appearences) == 0