junctions = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}

wires = {'battery': ('A', 'G'), ('A', 'B'): ('A', 'B'), ('A', 'E'): ('A', 'E'), ('B', 'C'): ('B', 'C'), ('B', 'F'): ('B', 'F'), ('C', 'D'): ('C', 'D'), ('C', 'G'): ('C', 'G'), ('D', 'A'): ('D', 'A'), ('D', 'H'): ('D', 'H'), ('E', 'F'): ('E', 'F'), ('F', 'G'): ('F', 'G'), ('G', 'H'): ('G', 'H'), ('H', 'E'): ('H', 'E')}

resistances = {'battery': 0, ('A', 'B'): 30, ('A', 'E'): 30, ('B', 'C'): 30, ('B', 'F'): 30, ('C', 'D'): 30, ('C', 'G'): 30, ('D', 'A'): 30, ('D', 'H'): 30, ('E', 'F'): 30, ('F', 'G'): 30, ('G', 'H'): 30, ('H', 'E'): 30}

voltages = {'battery': -300, ('A', 'B'): 0, ('A', 'E'): 0, ('B', 'C'): 0, ('B', 'F'): 0, ('C', 'D'): 0, ('C', 'G'): 0, ('D', 'A'): 0, ('D', 'H'): 0, ('E', 'F'): 0, ('F', 'G'): 0, ('G', 'H'): 0, ('H', 'E'): 0}

soln = {'battery': -12.0, ('A', 'B'): 4.0, ('A', 'E'): 4.0, ('B', 'C'): 2.0, ('B', 'F'): 2.0, ('C', 'D'): -2.0, ('C', 'G'): 4.0, ('D', 'A'): -4.0, ('D', 'H'): 2.0, ('E', 'F'): 2.0, ('F', 'G'): 4.0, ('G', 'H'): -4.0, ('H', 'E'): -2.0}
