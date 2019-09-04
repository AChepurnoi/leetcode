class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = dict()

        index = 0
        for c in s:
            if c in chars:
                data = chars[c]
                data['count'] += 1
                data['positions'].append(index)
            else:
                data = {'count': 1, 'positions': [index]}
                chars[c] = data
            index += 1
        
        positions = []
        for letter, data in chars.items():
            if data['count'] == 1:
                positions.extend(data['positions'])
            
        if len(positions) == 0:
            return -1
        else:
            return min(positions)