from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:

        faces = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                score = self._calculate_cell_faces(i, j, grid)
                faces = faces + score
        return faces

    def _calculate_cell_faces(self, i, j, grid):
        height = grid[i][j]
        faces = 0
        if height == 0:
            return 0
        # Bottom face
        faces += 1
        # Top face
        faces += 1

        cells = [
            [i + 1, j],
            [i - 1, j],
            [i, j + 1],
            [i, j - 1]

        ]

        for [ii, jj] in cells:
            if self.is_valid_cell(grid, ii, jj):
                faces = faces + max(0, height - grid[ii][jj])
            else:
                faces = faces + height
        return faces

    def is_valid_cell(self, grid, i, j):
        i_valid = 0 <= i < len(grid)
        if i_valid:
            j_valid = 0 <= j < len(grid[i])
            return j_valid
        else:
            return False


data = [
    [[2]],
    [[1, 2], [3, 4]],
    [[1, 0], [0, 2]],
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
    [[2, 2, 2], [2, 1, 2], [2, 2, 2]]

]

for d in data:
    r = Solution().surfaceArea(d)
    print(f"{d} -> {r}")
