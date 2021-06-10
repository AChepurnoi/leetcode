class Solution:
    def secondHighest(self, s: str) -> int:
        numbers = set()
        for c in s:
            if self.is_number(c):
                numbers.add(int(c))

        if len(numbers) <= 1:
            return -1
        else:
            biggest = -1
            second_biggest = -1
            for n in numbers:
                if n > biggest:
                    second_biggest = biggest
                    biggest = n
                elif n > second_biggest:
                    second_biggest = n

            return second_biggest

    def is_number(self, i):
        return "0" <= i <= "9"


data = [
    "dfa12321afd",
    "abc1111",
    "sjhtz8344"
]

for d in data:
    r = Solution().secondHighest(d)
    print(f"{d} -> {r}")
