class Solution:
    # Array of Fixed Length
    # Time complexity and Space complexity O(N2)
    def isValidSudoku(self, board):
        N = 9

        rows = [[0] * N for _ in range(N)]
        cols = [[0] * N for _ in range(N)]
        boxes = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] == '.':
                    continue
                pos = int(board[c][r]) -1

                if rows[r][pos] == 1:
                    return False
                rows[r][pos] = 1

                if cols[pos][c] == 1:
                    return False
                cols[pos][c] = 1

                idx = (r // 3) * 3 + c // 3
                if boxes[idx][pos] == 1:
                    return False
                boxes[idx][pos] = 1
            return True
    def isValidSudoku2(self, board):
        N = 9

        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                if val == '.':
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                idx = (r // 3) * 3 + c //3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
        return True