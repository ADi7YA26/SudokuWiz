import pyautogui, time

def solveSudoku(board):

    def isSafe(board, row, col, value):
        for i in range(9):
            if(board[row][i] == value):
                return False
            if(board[i][col] == value):
                return False
            if(board[3 * (row//3) + (i//3)][3*(col//3) + i%3] == value):
                return False
        
        return True   

    for row in range(9):
        for col in range(9):
            if(board[row][col] == 0):
                for value in range(1,10):
                    if(isSafe(board, row, col, value)):
                        board[row][col] = value

                        if(solveSudoku(board)):
                            return True
                        else: board[row][col] = 0

                return False    
    return True



def Print(board):

    def press(key):
        pyautogui.press(str(key))

    time.sleep(5) #time gap to start printing

    for row in range(9):
        for col in range(9):
            if(initialBoard[row][col] == 0):
                press(board[row][col])
            
            press("right")

            # if it's last column than move down to the next row
            if(col==8): 
                press("down")


if __name__ == "__main__":

    initialBoard = [list(map(int, input().split())) for r in range(9)]

    # Create deep copy of the sudoku grid 
    board = [[value for value in row] for row in initialBoard]

    solveSudoku(board)
    Print(board)

