import sys
sys.setrecursionlimit(10000)

# NO OTHER IMPORTS!


##################################################
#  Problem 1
##################################################

def max_diff_index(nums):
    """ Given the list of numbers nums with at least
        two numbers, returns the index 
        i that maximizes the absolute value of the difference 
        between the ith and (i-1)th element, 
        i.e., | nums[i] - nums[i-1] |.


        If there are multiple such indices, returns any 
        of them.
    """
    maxDiff = 0
    ith = 0
    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i-1]) > maxDiff:
            maxDiff = abs(nums[i] - nums[i-1])
            ith = i
    return ith


##################################################
#  Problem 2
##################################################

def replace_parallels(wires, resistances):
    """ Returns a new circuit representation in which wires in parallel are 
        replaced with single wires.

        Inputs:

            wires: a dictionary mapping a unique wire ID (a string or tuple) 
                   to a tuple of two elements representing the two junctions, 
                   in any order, which it connects. Junctions are themselves 
                   strings or tuples. 

            resistances: a dictionary mapping a wire ID to a numeric value 
                         representing the magnitude of the resistance of the 
                         wire in Ohms. It has the same set of keys as `wires`. 
                         You may assume no resistance is zero.

        Returns a tuple (new_wires, new_resistances) of dictionaries of the same
        format as the inputs, representing a circuit equivalent to the given one,
        but with no wires in parallel.
        
        Example: wires = {'0': ('A', 'B'), '1': ('B', 'C'), '2': ('C', 'A'), '3': ('A', 'C')}
                 resistances = {'wire1': 2, 'wire2': 4}

                 One valid solution is
                 new_wires = {'wire1': ('A', 'B')}
                 new_resistances = {'wire1': 4 / 3}
    """
    newWires = {}
    newResistances = {}
    uniqueWires = []
    
    wiresCopy = wires.copy()
    for wire in wires.keys():
        theTuple = wires[wire]
        first = theTuple[0]
        second = theTuple[1]
        count = 0
        for w in wiresCopy.keys():
            t = wires[w]
            if (first in t) and (second in t):
                count += 1
                
        if count > 1:
            del wiresCopy[wire]
        
    newWires = wiresCopy
    for wire in newWires.keys():
        theTuple = newWires[wire]
        first = theTuple[0]
        second = theTuple[1]
        total = 0
        for w in wires.keys():
            t = wires[w]
            if (first in t) and (second in t):
                r = resistances[w]
                total += 1.0/r
            

        newResistances[wire] = 1.0/total
    print("!!!!!!", newResistances)
    return (newWires, newResistances)



##################################################
#  Problem 3
##################################################
def count_ones_and_zeroes(peg_board):
    ones = 0
    zeroes = 0
    for i in peg_board:
        if i == 1:
            ones += 1
        else:
            zeroes += 1
    return (ones, zeroes)

def no_more_valid_moves(ones, peg_board):

    # [1, 1, 0]
    if ones == len(peg_board):
        return True
    elif ones == 1:
        return True
    for i in range(2, len(peg_board)):
        if peg_board[i] == 0 and peg_board[i-1] == 1 and peg_board[i-2] == 1:
            return False
        elif peg_board[i] == 1 and peg_board[i-1] == 1 and peg_board[i-2] == 0:
            return False
    print("down here")
    return True

def update_board(peg_board):
    for i in range(0, len(peg_board) - 2):
        
        if peg_board[i] == 1 and peg_board[i+1] == 1 and peg_board[i+2] == 0:
            peg_board[i+2] = 1
            peg_board[i+1] = 0
            peg_board[i] = 0
            break
        elif peg_board[i] == 0 and peg_board[i+1] == 1 and peg_board[i+2] == 1:
            peg_board[i+2] = 0
            peg_board[i+1] = 0
            peg_board[i] = 1
            break
    return peg_board

def minimum_pegs(peg_board):
    """ Returns the minimum number of pegs that could be reached on
        the given peg board using valid peg solitaire moves.

        peg_board: a list representing a 1D peg board, where 1s are
                   holes with pegs and 0s are empty holes.
    """
    count = count_ones_and_zeroes(peg_board)
    ones = count[0]
    zeroes = count[1]
    
    if no_more_valid_moves(ones, peg_board):
        print("base case", ones)
        return ones
    
    new_board = update_board(peg_board)
    print(new_board)
    return minimum_pegs(new_board)
    


if __name__ == "__main__":
    pass