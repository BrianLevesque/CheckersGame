from numpy import random
from numpy import reshape
from numpy import transpose

'''build_board which takes a parameter representing the size of the board;
 e.g. if 3 is passed in, the function will generate a 3x3 board. 
 The function will then use numpy to populate each cell of the board 
 randomly with one of the following strings: ‘Empty’, ‘Red’, ‘Black’. 
 The function will then return the newly created board.
'''

def build_board(size):
    #use numpy to populate each cell of the board
    #randomly with one of the following strings: ‘Empty’, ‘Red’, ‘Black’
    board = random.choice(['empty','red','black'],(size,size))

    return board
'''get_count which takes two parameters: A board and a string of either Empty, Red, or Black. 
It will return how many of that item exists in the board.
'''

def get_count(board, str):

    count = (board == str).sum()

    return count

print (f"Testing out checkers' __name__ variable. Here's what's in it: {__name__}.")


#Add a function that changes the size of the board.
def change_size(board, size1,size2):
    return reshape(board,(size1, size2))

#Add a function that pivots the board so that rows become columns and vice versa.
def swap_axis(board):
    return transpose(board)