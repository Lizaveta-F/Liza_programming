import random
import keyboard
import argparse
import numpy as np
import pickle
import copy

parser = argparse.ArgumentParser()
parser.add_argument("--size", default=4, help="Enter the number of rows and columns")
parser.add_argument("--width", default=6, help="Enter the width of the grid")
parser.add_argument("--height", default=1, help="Enter the height of the grid")
args = parser.parse_args()

n_cols = int(args.size)
n_rows = int(args.size)
w_cell = int(args.width)
h_cell = int(args.height)    

def show_state(state):
    
    matrix = state['matrix'] 
    score = state['score']
    best_score = state['best_score']
    hor_line = ('+' + '-' * w_cell) * n_cols + '+\n'
    line_with_gaps = ('|' + '%s') * n_cols + '|\n'
    table = (hor_line + line_with_gaps * h_cell) * n_rows + hor_line
    
    print(table % tuple((str(cell).center(w_cell, ' ') for row in matrix for cell in row)))
    # TODO добавьте отображение текущего и лучшего score??????
    print(f"Your current score is {score}")
    print(f"Your best score is {best_score} ")

def step(state, cmd):
    n_turns = { # main direction is left
        'w': (1, 3),
        'a': (0, 0),
        's': (3, 1),
        'd': (2, 2),
        'W': (1, 3),
        'A': (0, 0),
        'S': (3, 1),
        'D': (2, 2),
        'up': (1, 3),
        'left': (0, 0),
        'down': (3, 1),
        'right': (2, 2),
    }
    before = n_turns[cmd][0]
    after = n_turns[cmd][1]
    matrix = state['matrix']
    
    
    matrix = turn(matrix, before)
    matrix = remove_zeros(matrix)
    matrix, step_score = aggregation(matrix)
    matrix = append_zeros(matrix)
    matrix = randomize(matrix)
    matrix = turn(matrix, after)
    
    state['score'] += step_score
    state['matrix'] = matrix
    state = update_best_score(state)
    
def turn(matrix,k):
    matrix =  np.rot90(matrix,k=k)
    matrix=matrix.tolist()   
    return matrix
        
def remove_zeros(matrix):
    for i in matrix:
        while 0 in i:
            i.remove(0)
    return matrix

def aggregation(matrix):
    
    step_score = 0
    for i in matrix: 
        for x in range(len(i)-1):
            last_num = i[x]
            if i[x+1] == last_num:
                i[x] = i[x+1] * 2
                step_score += i[x]
                i[x+1]=0
            
    return matrix,step_score

def append_zeros(matrix):
    for i in matrix:
        while len(i)<int(args.size):
            i.append(0)
    return matrix
    
def randomize(matrix):
    numNeeded = 1
    while numNeeded > 0:
        x=random.randrange(int(args.size))
        y=random.randrange(int(args.size))
        if matrix[x][y] == 0:
            matrix[x][y] = random.choice([2, 4])
            numNeeded -= 1
    return matrix    

def save_state(state):
    with open('state.pkl', 'wb') as fh:
    	pickle.dump(state, fh)
    return state

def load_state(state):
    with open('state.pkl', 'rb') as fh:
        state = pickle.load(fh)
    return state

def update_best_score(state):
    if state['score'] > state['best_score']:
        state['best_score'] = state['score']
    return state
    
def won(matrix):
    for row in matrix:
        if 2048 in row:
            return True
    return False

def exit_game():
    print("Good bye, see you next time")
    
        

def event(state, cmd):
    validInput = True
    
    if cmd == 'esc':
        exit_game()    
    elif cmd == 'n':
        print("Welcome to new game")
        state = print(init_state())    
    elif cmd in ("w","W","a","A","d","D","s","S","left","right","up","down"):
        step(state, cmd)    
    else:
        validInput = False
    if not validInput:
        print("Try again, please")
        
    return state

    
def generate_state():
    matrix = [
        [0 for _ in range(4)] for _ in range(4)]
    matrix = randomize(matrix)
    return matrix

def init_state():
    state = dict()
    state['matrix'] = generate_state() # matrix 4x4 with initial number "2" in random cell
    state['score'] = 0
    state['best_score'] = load_state(state)['best_score'] # read best score from some file
    # state['is_finished'] = False
    return state
    
def run():
    gameOver = False
    state = init_state()
    show_state(state)
    tempmatrix= copy.deepcopy(state['matrix'])
    while not gameOver:
        e = keyboard.read_event()
        if e.event_type != 'up': continue # handling keys push up
        cmd = e.name
        state = event(state, cmd)
        show_state(state)
        save_state(state)
        load_state(state)
        update_best_score(state)
        if tempmatrix==state['matrix']:
            print("Sorry, you lost the game")
            gameOver = True  
        elif won(state['matrix'])==True:
            print("You won! Congratulations!")
            print("If you wish to start a new game, please, press the button 'n', if not, please, press 'Esc' button")
            gameOver = True
            
            
        
if __name__ == '__main__':
    run()