#Commented part is backtracking
#For backtracking uncomment from line 8 to 27
#and comment lines 30 to 36

def solve_n_queens(n):
    chessboard = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    # def is_safe(row, col):
    #     for i in range(row):
    #         if chessboard[i][col] == 'Q':
    #             return False
            
    #     i , j = row - 1, col - 1
    #     while i >= 0 and j >= 0:
    #         if(chessboard[i][j] == 'Q'):
    #             return False
    #         j = j - 1
    #         i = i - 1

    #     i , j = row - 1, col + 1
    #     while i >= 0 and j < n:
    #         if(chessboard[i][j] == 'Q'):
    #             return False
    #         j = j + 1
    #         i = i - 1
        
    #     return True
    
    def is_safe(row, col):
        for i in range(row):
            if chessboard[i][col] == 'Q' or\
            ((i + col - row) >= 0 and chessboard[i][i + col - row] == 'Q') or\
            ((col - i + row) < n and chessboard[i][col - i + row] == 'Q'):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append([' '.join(row) for row in chessboard])
            return
        
        for col in range(n):
            if is_safe(row, col):
                chessboard[row][col] = 'Q'
                backtrack(row + 1)
                chessboard[row][col] = '.'

    backtrack(0)
    return solutions
                
n = 4
solution = solve_n_queens(n)
for solution in solution:
    for row in solution:
        print(row)
    print()

