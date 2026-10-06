class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        total_elements = rows * cols

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0

        r, c = 0, 0
        visited = set()
        res = []

        while len(res) < total_elements:
            res.append(matrix[r][c])
            visited.add((r, c))

            next_r = r + directions[d][0]
            next_c = c + directions[d][1]

            if (next_r < 0 or next_r >= rows or
                next_c < 0 or next_c >= cols or
                (next_r, next_c) in visited):
                d = (d + 1) % 4

            r += directions[d][0]
            c += directions[d][1]

        return res