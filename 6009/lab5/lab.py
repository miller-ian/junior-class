"""6.009 Lab 5 -- Don't Turn Left!"""

# NO ADDITIONAL IMPORTS

def get_neighbors(edges, node):
    neighbors = []

    for edge in edges:
       if edge["start"] == node: 
            neighbors.append(edge["end"])
    return neighbors

def get_neighbors_noleft(edges, node):
    neighbors = []
    potentialNeighbors = []
    for edge in edges:
        if edge["start"] == node and (node[0] >= edge["end"][0]): #this checks if neighbor is to the left of the current node
            print(node)
            potentialNeighbors.append(edge["end"])
    return potentialNeighbors

def get_neighbors_kleft(edges, node, k):
    neighbors = []
    potentialNeighbors = []
    for edge in edges:
        if edge["start"] == node and (node[0] >= edge["end"][0]) and count > 0:
            potentialNeighbors.append(edge["end"], True) #True is neighbor is left turn
        elif edge["start"] == node:
            potentialNeighbors.append(edge["end"], False) #False means neighbor is not left turn
         
    return potentialNeighbors, 

def fix_format(edges, aListOfTuples):
    '''
    Takes in a list of coordinates and puts that list into the format that edges are read.
    '''
    returnList = []
    for i in range(len(aListOfTuples)-1):
        aDict = {}
        start = aListOfTuples[i]
        end = aListOfTuples[i+1]
        aDict["start"] = start
        aDict["end"] = end
        returnList.append(aDict)

    return returnList

def shortest_path(edges, start, end):
    """
    Finds a shortest path from start to end using the provided edges

    Args:
        edges: a list of dictionaries, where each dictionary has two items. 
            These items have keys `"start"` and `"end"` and values that are 
            tuples (two integers), to specify grid locations.
        start: a tuple representing our initial location.
        end: a tuple representing the target location.

    Returns:
        A list containing the edges taken in the resulting path if one exists, 
            None if there is no path

        formatted as:
            [{"start":(x1,y1), "end":(x2,y2)}, {"start":(x2,y2), "end":(x3,y3)}]
    """
    visitedNodes = []
    queue = [[start]]
    if start == end:
        return [start]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visitedNodes:
            neighbors = get_neighbors(edges, node)
            for neighbor in neighbors:
                newPath = list(path)
                newPath.append(neighbor)
                queue.append(newPath)
                if neighbor == end:
                    return fix_format(edges, newPath)
            visitedNodes.append(node)
    return None

def shortest_path_no_lefts(edges, start, end):
    """
    Finds a shortest path without any left turns that goes
        from start to end using the provided edges. 
        (reversing turns are also not allowed)

    Args:
        edges: a list of dictionaries, where each dictionary has two items. 
            These items have keys `"start"` and `"end"` and values that are 
            tuples (two integers), to specify grid locations.
        start: a tuple representing our initial location.
        end: a tuple representing the target location.

    Returns:
        A list containing the edges taken in the resulting path if one exists, 
            None if there is no path

        formatted as:
            [{"start":(x1,y1), "end":(x2,y2)}, {"start":(x2,y2), "end":(x3,y3)}]
    """
    visitedNodes = []
    queue = [[start]]
    if start == end:
        return [start]
    
    while queue:
        path = queue.pop(0) #pops off last element in queue
        node = path[-1] #takes last element in path
        if node not in visitedNodes:
            neighbors = get_neighbors_noleft(edges, node)
            for neighbor in neighbors:
                newPath = list(path)
                newPath.append(neighbor)
                queue.append(newPath)
                if neighbor == end:
                    return fix_format(edges, newPath)
            visitedNodes.append(node)
    return None

def shortest_path_k_lefts(edges, start, end, k):
    """
    Finds a shortest path with no more than k left turns that 
        goes from start to end using the provided edges.
        (reversing turns are also not allowed)

    Args:
        edges: a list of dictionaries, where each dictionary has two items. 
            These items have keys `"start"` and `"end"` and values that are 
            tuples (two integers), to specify grid locations.
        start: a tuple representing our initial location.
        end: a tuple representing the target location.
        k: the max number of allowed left turns.

    Returns:
        A list containing the edges taken in the resulting path if one exists, 
            None if there is no path

        formatted as:
            [{"start":(x1,y1), "end":(x2,y2)}, {"start":(x2,y2), "end":(x3,y3)}]
    """
    visitedNodes = []
    queue = [[start]]
    if start == end:
        return [start]
    count = k
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visitedNodes:
            if count > 0:
                neighbors = get_neighbors_kleft(edges, node)
            for neighbor in neighbors:
                newPath = list(path)
                newPath.append(neighbor)
                queue.append(newPath)
                if neighbor == end:
                    return fix_format(edges, newPath)
            visitedNodes.append(node)
    return None


if __name__ == "__main__":
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used for testing.
    pass


