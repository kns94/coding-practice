class Solution(object):

    def __init__(self):
        self.dp = {}

    def recUpdate(self, board, pos):
        r, c = len(board), len(board[0])

        if pos[0] >= r or pos[0] < 0:
            return board

        if pos[1] >= c or pos[1] < 0:
            return board

        if tuple(pos) in self.dp:
            return board
        elif board[pos[0]][pos[1]] == 'M':
            self.dp[tuple(pos)] = 'M'
            return board
        else:
            mineCount = 0

            #Top
            if pos[0] - 1 >= 0:
                if board[pos[0] - 1][pos[1]] == 'M':
                    mineCount += 1

            #Bottom
            if pos[0] + 1 < r:
                if board[pos[0] + 1][pos[1]] == 'M':
                    mineCount += 1

            #Right
            if pos[1] + 1 < c:
                if board[pos[0]][pos[1] + 1] == 'M':
                        mineCount += 1
            
            #Left
            if pos[1] - 1 >= 0:
                if board[pos[0]][pos[1] - 1] == 'M':
                        mineCount += 1

            #Top-left
            if pos[0] - 1 >=0 and pos[1] - 1 >= 0:
                if board[pos[0] - 1][pos[1] - 1] == 'M':
                        mineCount += 1

            #Top-right
            if pos[0] - 1 >=0 and pos[1] + 1 < c:
                if board[pos[0] - 1][pos[1] + 1] == 'M':
                        mineCount += 1        

            #Bottom-left
            if pos[0] + 1 <r and pos[1] - 1 >= 0:
                if board[pos[0] + 1][pos[1] - 1] == 'M':
                        mineCount += 1

            #Bottom-right
            if pos[0] + 1 <r and pos[1] + 1 <c:
                if board[pos[0] + 1][pos[1] + 1] == 'M':
                        mineCount += 1

            if mineCount == 0:
                self.dp[tuple(pos)] = 'B'
                board[pos[0]][pos[1]] = 'B'
                board = self.recUpdate(board, [pos[0] - 1, pos[1]])
                board = self.recUpdate(board, [pos[0] + 1, pos[1]])
                board = self.recUpdate(board, [pos[0], pos[1] + 1])
                board = self.recUpdate(board, [pos[0], pos[1] - 1])
                board = self.recUpdate(board, [pos[0] - 1, pos[1] - 1])
                board = self.recUpdate(board, [pos[0] - 1, pos[1] + 1])
                board = self.recUpdate(board, [pos[0] + 1, pos[1] - 1])
                board = self.recUpdate(board, [pos[0] + 1, pos[1] + 1])
            else:
                self.dp[tuple(pos)] = str(mineCount)
                board[pos[0]][pos[1]] = str(mineCount)

        return board

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
        r, c = len(board), len(board[0])
        ms = {}

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        board = self.recUpdate(board, click)
        return board

board = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

board = [["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","M"],["E","E","M","E","E","E","E","E"],["M","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","M","E","E","E","E"]]
click = [0, 0]
print '\n\n'

for b in board:
    print b

print '\n\n'
print Solution().updateBoard(board, click)
