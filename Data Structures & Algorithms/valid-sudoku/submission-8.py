class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9):
            for c in range (9):

                num = board[r][c]

                if num == ".":
                    continue

                if (num in rows[r]
                    or num in col[c]
                    or num in grid[(r//3, c//3)]):
                    return False

                rows[r].add(num)
                col[c].add(num)
                grid[(r//3, c//3)].add(num)

        return True  