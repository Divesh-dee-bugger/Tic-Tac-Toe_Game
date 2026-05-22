from Griding.grid import Grid
from art import tprint

def greet():
    try:
        tprint("The    Tic-Tac-Toe    Game")
    except:
        print("Welcome to the Tic-Tac-Toe Game!")
    print("Made with 💖 by Divesh\n\n")
    print("How To Play:")
    print("-Just go through the Reference Grid given below to see which number corresponds to which cell.")
    print("-When it's your turn, just enter the number corresponding to the cell you want to mark with your symbol(X or O).")
    print("-Turns keep switching between the two players until one of them wins or it's a draw.")
    print("\nGood Luck!\n\n")

def main():

    greet()

    grid = Grid(3, 3)


    grid.addVal(1, 1, "1")
    grid.addVal(2, 1, "2")
    grid.addVal(3, 1, "3")

    grid.addVal(1, 2, "4")
    grid.addVal(2, 2, "5")
    grid.addVal(3, 2, "6")

    grid.addVal(1, 3, "7")
    grid.addVal(2, 3, "8")
    grid.addVal(3, 3, "9")


    print("Reference Grid:")
    grid.printGrid()
    print("")

    grid.clear()

    print("Game Grid:")
    grid.printGrid()
    print("")


    nums = {
        "1": (1, 1),
        "2": (2, 1),
        "3": (3, 1),
        "4": (1, 2),
        "5": (2, 2),
        "6": (3, 2),
        "7": (1, 3),
        "8": (2, 3),
        "9": (3, 3)
    }



    current_player = "X"

    while True:
        turn = input(f"Enter for {current_player}: ")
        coordinate = nums[turn]

        if grid.getVal(coordinate[0], coordinate[1]) in ["X", "O"]:
            print("Already taken")
            continue

        grid.addVal(coordinate[0], coordinate[1], current_player)

        grid.printGrid()

        isWin = check_win(grid)
        isDraw = checkDraw(grid)

        if isDraw == True:
            print("It's a draw!")
            break

        if isWin == True:
            print(f"{current_player} wins!")
            break


        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    
    input("Press Enter to Exit...")

    


def check_win(grid):


    # Horizontal Check
    
    for y in range(1, 4):
        if grid.getVal(1, y) == grid.getVal(2, y) == grid.getVal(3, y) != "":
            return True


    # Vertical Check

    for x in range(1, 4):
        if grid.getVal(x, 1) == grid.getVal(x, 2) == grid.getVal(x, 3) != "":
            return True
        

    # Diagonal Check

    ## 1st Diagonal
    if grid.getVal(1, 1) == grid.getVal(2, 2) == grid.getVal(3, 3) != "":
        return True
    
    ## 2nd Diagonal
    if grid.getVal(1, 3) == grid.getVal(2, 2) == grid.getVal(3, 1) != "":
        return True
    

    return False


def checkDraw(grid):

    for x in range(1, 4):
        for y in range(1, 4):
            if grid.getVal(x, y) == "":
                return False
            
    return True



if __name__ == "__main__":
    main()


