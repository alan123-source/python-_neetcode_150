#this a sudoku like problem with condition
# that everey row or coloumn should not contain
# any duplicates such that for a 3 by 3 grid every
# single grid should not
# containi any duplicates we use hash
# set for this remember for finding duplictaes
# we always use hash set
import collections
class Solution:
    def issudokuo(self,board:list[list[str]]) ->bool:
        cols=collections.defaultdict(set)
        rows=collections.defaultdict(set)
        square=collections.defaultdict(set) #key=(r/3,c/3)
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3,c//3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])

        return True
sol=Solution()
print(sol.issudokuo([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]))
# key takeaways 1 .use hash set for finding duplicates
# 2. how to iterate in a muliple array
# 3. subdivision dividing a matrix into subgroups
# 4.handling myultiple constraints
