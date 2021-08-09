      #recursive function
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True #means solution has been found
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)): #plugs in value to board if its valid
            bo[row][col] = i

            if solve(bo): #finishes the solution by recursively calling solve into board using value added until solution is found
                return True

            bo[row][col] = 0 #goes to last elememt if its not correct

    return False


def valid(bo, num, pos):  #function to find if the sudoku board is valid
    # checks the row
    for i in range(len(bo[0])):  #checks the row and loops through each column
        if bo[pos[0]][i] == num and pos[1] != i: #checks if each element in the row is equal to the number added in and ignores if its the inserted position
            return False

    # checks the column
    for i in range(len(bo)): #checks the column and loops through each row (0 to 8)
        if bo[i][pos[1]] == num and pos[0] != i: #checks if each element in the column is equal to the number added in and ignores if its the inserted position
            return False

    # Check box
    box_x = pos[1] // 3 # value 0, 1 or 2
    box_y = pos[0] // 3
 #loops through each element in the 9 boxes 
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False  #false for duplicate

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ") #for printing a line after every 3rd row

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None