def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, n, 1), range(col, -1,-1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col, n):
    if col>= n:
        return True
    
    for row in range(len(board)):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            
            if solve_n_queens_util(board, col+1, n):
                return True
            board[row][col] = 0
    
    return False
        
def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    if not solve_n_queens_util(board, 0, n):
        print("Solution Does Not Exist")
        return False
    
    print_board(board)
    return True


def print_board(board):
    for row in board:
        print(" ".join("Q" if x ==1 else "." for x in row))
    print("\n")
    
n = 8
solve_n_queens(n)
    
    
"""
Extras: 
for i in range(8):
    print(" ".join("Q"))

board = [[0 for _ in range(9)] for _ in range(9)]
print(board)


for i in range(7,-1,-1):
    print(i)
    
for i in range(4,8,1):
    print(i)
"""