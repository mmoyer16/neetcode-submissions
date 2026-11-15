class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for num in range(9)]
        cols = [set() for num in range(9)]
        box = [set() for num in range(9)]

        for r in range(9):
            for c in range(9):
                d = board[r][c]
                b = (r // 3) * 3 + (c // 3)
                if d in rows[r] or d in cols[c] or d in box[b]:
                    return False
                if d != '.':
                    rows[r].add(d)
                    cols[c].add(d)
                    box[b].add(d)

        return True
