
import pickle
import random
import copy
import argparse
import keyboard
import json


parser = argparse.ArgumentParser()
parser.add_argument("--size", default=4, help="Enter the size")
args = parser.parse_args()
size = args.size

boardSize = int(size)


def display():
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    numSpaces = len(str(largest))

    for row in board:
        currRow = "|"
        for element in row:
            if element == 0:
                currRow += " "*numSpaces + "|"
            else:
                currRow += (" "*(numSpaces - len(str(element)))) + str(element) + "|"
        print(currRow)
    print()



def mergeOneRowL(row):
    global score
    score = 0
    for _ in range(boardSize-1):
        for i in range(boardSize-1, 0, -1):  # shift from right to left
            if row[i-1] == 0:  # check if there is a zero
                row[i-1] = row[i]
                row[i] = 0
    # Merge the Value

    for i in range(boardSize-1):
        if row[i] == row[i+1]:  # check if the element is the same as the nearest one
            row[i] *= 2
            row[i+1] = 0
            score += row[i]
            

    for i in range(boardSize-1, 0, -1):
        if row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0
    return row

def save_state(state):
    with open('state.pkl', 'wb') as fh:
    	pickle.dump(state, fh)
#     score=mergeOneRowL(score)
#     with open('score.txt', 'w') as fh:
#         json.dump(score,fh)
#     with open('score.txt','r') as json_file:
#         score = json.loads(json_file.read())    
#     print(f"Your score is {score}")
    

def merge_left(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])
    return currentBoard


def reverse(row):
    new = []
    for i in range(boardSize - 1, -1, -1):
        new.append(row[i])
    return new


def merge_right(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])
    return currentBoard


def transpose(currentBoard):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = currentBoard[j][i]
                currentBoard[j][i] = currentBoard[i][j]
                currentBoard[i][j] = temp
    return currentBoard


def merge_up(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = merge_left(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard


def merge_down(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = merge_right(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard

def pickNewValue():
    if random.randint(1, 8) == 1:
        return 4
    else:
        return 2


def addNewValue():
    rowNum = random.randint(0, boardSize-1)
    colNum = random.randint(0, boardSize-1)

    while not board[rowNum][colNum] == 0:
        rowNum = random.randint(0, boardSize-1)
        colNum = random.randint(0, boardSize-1)

    board[rowNum][colNum] = pickNewValue()


def won():
    for row in board:
        if 2048 in row:
            return True
    return False


def noMoves():
    tempBoard1 = copy.deepcopy(board)
    tempBoard2 = copy.deepcopy(board)

    tempBoard1 = merge_down(tempBoard1)
    if tempBoard1 == tempBoard2:
        tempBoard1 = merge_up(tempBoard1)
        if tempBoard1 == tempBoard2:
            tempBoard1 = merge_left(tempBoard1)
            if tempBoard1 == tempBoard2:
                tempBoard1 = merge_right(tempBoard1)
                if tempBoard1 == tempBoard2:
                    return True
    return False


board = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    board.append(row)

numNeeded = 2

while numNeeded > 0:
    rowNum = random.randint(0, boardSize-1)
    colNum = random.randint(0, boardSize-1)

    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = pickNewValue()
        numNeeded -= 1

display()

gameOver = False

while not gameOver:
    
    validInput = True

    tempBoard = copy.deepcopy(board)
    event = keyboard.read_event()
    if event.event_type != 'up': continue
    move = event.name
    if move in ("d","D","right"):
        board = merge_right(board)
    elif move in("a","A" ,"left"):
        board = merge_left(board)
    elif move in ("w", "W", "up"):
        board = merge_up(board)
    elif move in ("s","S","down"):
        board = merge_down(board)
    else:
        validInput = False

    if not validInput:
        print("Try again, please")
    else:
        if board == tempBoard:
            print("Try a differend direction")
        else:
            if won():
                display()
                print("You won! Congratulations!")
                gameOver = True
            else:
                addNewValue()
                display()
                # save_state(score)
                if noMoves():
                    print("Sorry, you lost the game")
                    gameOver = True
