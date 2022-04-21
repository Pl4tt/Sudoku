boards = [
    [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ],
    [
        [9,0,0,0,8,0,0,0,1],
        [0,0,0,4,0,6,0,0,0],
        [0,0,5,0,7,0,3,0,0],
        [0,6,0,0,0,0,0,4,0],
        [4,0,1,0,6,0,5,0,8],
        [0,9,0,0,0,0,0,2,0],
        [0,0,7,0,3,0,2,0,0],
        [0,0,0,7,0,5,0,0,0],
        [1,0,0,0,4,0,0,0,7]
    ],
    [
        [8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,0,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]
    ]
]


def solve(board):
    empty = get_empty(board)

    if empty is None:
        return True
    
    x, y = empty

    for val in range(1, 10):
        if is_valid(board, x, y, val):
            board[x][y] = val

            if solve(board):
                return True
            
            board[x][y] = 0
            
    return False

def get_empty(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                return (x, y)
    
    return None

def is_valid(board, x, y, val):
    # check row, col
    for coordinate in range(len(board)):
        if board[x][coordinate] == val and coordinate != y or board[coordinate][y] == val and coordinate != x:
            return False
    
    # check 3x3 box
    box_x = x // 3
    box_y = y // 3

    for row in range(box_x*3, box_x*3+3):
        for col in range(box_y*3, box_y*3+3):
            if board[row][col] == val and (x, y) != (row, col):
                return False
    
    return True

def all_invalid(board, x, y, val):
    result = []

    for coordinate in range(len(board)):
        if board[x][coordinate] == val and coordinate != y:  # row
            result.append((x, coordinate))
        if board[coordinate][y] == val and coordinate != x:  # col
            result.append((coordinate, y))
    
    # check 3x3 box
    box_x = x // 3
    box_y = y // 3

    for row in range(box_x*3, box_x*3+3):
        for col in range(box_y*3, box_y*3+3):
            if board[row][col] == val and (x, y) != (row, col):
                result.append((row, col))
    
    return result

def print_board(board, title="Sudoku Board"):
    print("-"*((19-len(title))//2), title, "-"*((19-len(title))//2))

    for row in range(len(board)):
        if row != 0 and row%3 == 0:
            print("---------------------")
            print(*board[row][:3], "|", *board[row][3:6], "|", *board[row][6:9])
        else:
            print(*board[row][:3], "|", *board[row][3:6], "|", *board[row][6:9])

    print("---------END---------")



if __name__ == "__main__":
    solve(boards[0])
    print_board(boards[0])