# import the entire checkers library.
import checkers


'''game function will ask the user for the size of the board and
 will call the build_board function. It will then print out the full board 
 (you can just print the variable out; no need for extra formatting). 
 It will next print out how many empty cells, how many red cells, 
 and how many black cells are in the board using a function from your checkers.py file.
'''
def game():
    size = int(input("How big would you like the board? "))
    board = checkers.build_board(size)
    print(board)
    print(f"There are {checkers.get_count(board,"empty")} empty spaces")
    print(f"There are {checkers.get_count(board,"red")} red spaces")
    print(f"There are {checkers.get_count(board,"black")} black spaces")

if __name__ == "__main__":
    game()



