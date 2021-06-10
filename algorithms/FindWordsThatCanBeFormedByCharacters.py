from collections import defaultdict
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charToCount = defaultdict(int)
        len_acc = 0
        for c in chars:
            counter = charToCount[c] + 1
            charToCount[c] = counter

        for word in words:
            isValid = self.check_word(word, charToCount.copy())
            if isValid:
                len_acc = len_acc + len(word)

        return len_acc
    def check_word(self, word: str, chatToCount) -> bool:
        for c in word:
            count = chatToCount[c]
            if count > 0:
                chatToCount[c] = count - 1
            else:
                return False
        return True

data = [
    [["cat", "bt", "hat", "tree"], "atach"],
    [["hello","world","leetcode"],  "welldonehoneyr"]
]

for d in data:
    r = Solution().countCharacters(d[0], d[1])
    print(f"{d[0]} + {d[1]} -> {r}")
