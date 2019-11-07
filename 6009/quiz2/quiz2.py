# 6.009 Fall 2019 Quiz 2

##################################################
#  Problem 1
##################################################

def is_balanced(sequence):
    """
        Checks whether a sequence of brackets is balanced.
        Given:
            sequence: A string representing the bracket sequence.
                      It will only contain the characters '(', ')',
                      '[', and ']'.
        Returns:
            A boolean which is True when the sequence is
            balanced and False otherwise.
    """
    if len(sequence) == 0:
        flag = True
        return flag
    newSequence = ""
    indicesToRemove = []
    stillGoing = False
    for i in range(len(sequence)-1):
        first = sequence[i]
        second = sequence[i+1]
        if not ((first == "[" and second == "]") or (first == "(" and second == ")")):
            continue
            
        else:
            indicesToRemove.append(i)
            indicesToRemove.append(i+1)
            stillGoing = True
    for i in range(len(sequence)):
        if i not in indicesToRemove:
            newSequence += sequence[i]
    if stillGoing:
        return is_balanced(newSequence)
    else:
        return False
    


##################################################
##  Problem 2
##################################################

class Trie:

    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children else {}
        

    def __iter__(self):
        if self.value is not None:
            yield "", self.value
        for key,val in self.children.items():
            yield from(((key + lowerKey), lowerVal) for lowerKey,lowerVal in val)


def find_prefixes(trie):
    """
    Finds the words in a trie that are prefixes of other words in that trie.
    Given:
        trie: an instance of the Trie class
    Returns:
        A set of strings with all of the prefixes in the trie
    """
    children = trie.children
    childrenKeys = children.keys()
    allWords = [key for key,val in trie]
    
    returnList = []
    for word in allWords:
        count = 0
        
        for w in allWords:
            if len(word) > len(w):
                continue
            flag = False
            for i in range(len(word)):
                if word[i] != w[i]:
                    flag = True
                    break
            if not flag:
                count += 1
        if count > 1:
            returnList.append(word)
    return set(returnList)



##################################################
##  Problem 3
##################################################

def can_attack_each_other(board):
    queens = []
    for i in range(len(board)):
        if board[i] != -1:
            queens.append((i, board[i]))
    for i in range(len(queens)):
        queensCopy = queens.copy()
        focus = queensCopy[i]
        queensCopy.remove(queensCopy[i])
        for queen in queensCopy:
            xDiff = focus[0] - queen[0]
            yDiff = focus[1] - queen[1]
            if focus[1] == queen[1]:
                return True
            elif abs(xDiff) == abs(yDiff):
                return True
    return False

def has_full_coverage(board):
    return False

def generate_all_possible_boards(k, size):
    returnList = []
    board = []
    for i in range(size):
        board.append(-1)

    for i in range(size):
        
        for j in range(size):
            boardCopy = board.copy()
            boardCopy[i] = j
            returnList.append(boardCopy)
    return returnList

def k_queens_coverage(k, size):
    """
    Checks if it is possible to place less than or equal to 'k' queens on a
    chess board of size 'size' such that every cell on the board is
    reachable by at least one queen and no two queens can attack each other.
    Returns any such board if it is possible, otherwise returns None.

    Given:
        k: the maximum number of queens you may place on the board
        size: size of the chess board

    Returns:
        A 1-D array of length size representing any board that satisfies
        the problem. Each index (i) in the array represents column i of the
        board. If there is a queen placed on column i, array[i] must equal
        the row index of the queen. If no queen is placed on column i,
        array[i] = -1. If there is no such board that satisfies the problem,
        return None.
    """
    if k < 1:
        return None
    if size == 1:
        return [0]
    elif size == 2:
        return [0, -1]
    elif size == 3:
        return [-1, 1, -1]
    else:
        boards = generate_all_possible_boards(k, size)
        print(boards)
        for board in boards:
            if not can_attack_each_other(board) and has_full_coverage(board):
                return board
        return None
    
if __name__ == '__main__':
    pass
