"""6.009 Lab 3 -- Circuit Solver."""

# NO IMPORTS ALLOWED!

# Uncomment below and comment/rename the solveLinear defined in this file to
# use the sample solveLinear function.
# Remember to comment it out before submitting!

#from solve_linear_sample import solveLinear

def remove_zeroes(aDict):
    final = {}
    for i in aDict.keys():
        if aDict[i] != 0.0:
            final[i] = aDict[i]
    return final

def substituteEquation(equation, substitutedVariable, substitutionEquation):
    """
        Note that implementing this function is optional. You might want to
        consider implementing it to break up your code into more managable
        chunks.
        
        Given:
            equation: An equation represented by a dictionary that maps the
                      variables or 1 to its coefficient in the equation.
                      E.g. {1: 2, 'x': 2, 'y': 3} represents 2 + 2x + 3y = 0.
            substitutedVariable: The variable to be substituted out of the
                                 equation.
            substitutionEquation: The substitution equation represented as a
                                  dictionary.
        Return:
            finalEquation: A dictionary representing the resulting equation
                           after the substitution is performed. 
    """

    finalDict = {}
    firstHolder = {}
    secondHolder = {}
    divisor = substitutionEquation[substitutedVariable]
    for i in substitutionEquation.keys():
        firstHolder[i] = -substitutionEquation[i]/divisor
    try:
        multiplier = equation[substitutedVariable]
    except:
        multiplier = 1
    for i in firstHolder.keys():
        secondHolder[i] = firstHolder[i] * multiplier
    someKeys = secondHolder.keys()
    for i in equation.keys():
        if i in someKeys:
            finalDict[i] = equation[i] + secondHolder[i]
        else:
            finalDict[i] = equation[i]
    for i in someKeys:
        if i not in finalDict.keys():
            finalDict[i] = secondHolder[i]
    return remove_zeroes(finalDict)

def solve(equation):
    var = None
    val = 0
    divisor = 1
    for element in equation.keys():
        if type(element) == tuple or type(element) == str:
            var = element
            divisor = equation[element]
        else:
            val = equation[element]
    return (var, val/-divisor)

def plug(equations, aTuple):
    var = aTuple[0]
    val = aTuple[1]
    returnList = []
    
    for equation in equations:
        newEquation = equation

        for variable in equation.keys():
            oldVal = equation[variable]
            if variable == var:
                newVal = oldVal * val
                oldNum = 0
                try:
                    oldNum = equation[1]
                except:
                    continue
                newEquation[1] = newVal + oldNum
                newEquation[var] = False
        
        trimmedEquation = {}
        for variable in newEquation.keys():
            if newEquation[variable]:
                trimmedEquation[variable] = newEquation[variable]
               
        
        if trimmedEquation:
            returnList.append(trimmedEquation)

    return returnList
        

def getAssignment(variables, equations):
    if len(equations) == 1:
        theDict = remove_zeroes(equations[0])
        aTuple = solve(theDict)
        return aTuple
        

    substitutionEquation = None
    numVariables = 0
    for equation in equations:
        num = len(equation.keys())
        if num < numVariables:
            numVariables = num
            substitutionEquation = equation
    numVars = 0
    for key in substitutionEquation.keys():
        if (isinstance(key, tuple) or isinstance(key, str)):
            numVars += 1
    
    if (numVars == 1):
        returnStuff = solve(substitutionEquation)
        return returnStuff
    substitutionVar = None
    coefficient = 0
    for var in substitutionEquation.keys():
        if substitutionEquation[var] > coefficient and (isinstance(var, tuple) or isinstance(var, str)):
            substitutionVar = var
            coefficient = substitutionEquation[var]
    newEquations = []
    for equation in equations:
        equationDict = substituteEquation(equation, substitutionVar, substitutionEquation)
        if equationDict:
            newEquations.append(equationDict)
    
    nextEquations = []
    for equation in newEquations:
        if equation:
            nextEquations.append(equation)
    return getAssignment(variables, nextEquations)

def solveLinear(variables, equations):
    """
        Given:
            variables: A set of strings or tuples representing the independent
                       variables. E.g. {'x', 'y', 'z'}
            equations: A list of linear equations where each equation is
                       represented as a dictionary. Each dictionary maps the
                       variables or 1 to its coefficient in the equation.
                       E.g. {1: 2, 'x': 2, 'y': 3} represents 2 + 2x + 3y = 0.
                       Note that all variables may not appear in all of the
                       equations. Moreover, you may assume that the equations
                       are independent.
        Return:
            result: A dictionary mapping each variable to the numerical value
            that solves the system of equations. Assume that there is exactly
            one solution. Some inaccuracy as typical from floating point
            computations will be acceptable.
    """
    returnList = []
    iterations = len(variables)
    for i in range(iterations):
        returnDict = {}
        result = getAssignment(variables, equations)
        
        var = result[0]
        val = result[1]
        returnDict[var] = val 
        
        newEquations = plug(equations, (var, val))
        flag = True
        for eq in newEquations:

            if (len(eq) == 2) and (1 in eq.keys()):
                returnStuff = solve(eq)
                var = returnStuff[0]
                val = returnStuff[1]
                final = {}
                final[var] = val
                returnList.append(final)
                
                break
        
           
        equations = newEquations
        returnList.append(returnDict)
    
    
    finalDict = {}
    super_dict = {}
    for k in set(k for d in returnList for k in d):
        super_dict[k] = [d[k] for d in returnList if k in d]
    for i in super_dict.keys():
        finalDict[i] = super_dict[i][0]
    return finalDict
    

    
    
def solveCircuit(junctions, wires, resistances, voltages):
    """
        Given:
            junctions:  A set of junctions. Each junction is labeled by a string
                        or a tuple.
            wires:      A dictionary mapping a unique wire ID (a string or tuple)
                        to a tuple of two elements representing the starting and
                        ending junctions of the wire, respectively. The set of
                        wire IDs is disjoint from the set of junction labels.
                        Note that although electricity can flow in either
                        directions, each wire between a pair of junctions will
                        appear exactly once in the list. Moreover, the starting
                        and ending junctions are distinct.
            resistances:A dictionary mapping each unique wire ID to a numeric
                        value representing the magnitude of the resistance of
                        the wire in Ohms. This dictionary has the same set of
                        keys as the wires dictionary.
            voltages:   A dictionary mapping each unique wire ID to a numeric
                        value representing the voltage (EMF or potential
                        difference) of the battery connected along the wire in 
                        Volts. The positive terminal of the battery is next to
                        the ending junction (as defined in the wires dictionary)
                        if the voltage is positive whereas it is next to the 
                        starting junction otherwise. This dictionary also has
                        the same set of keys as the wires dictionary.
        Return:
            result: A dictionary mapping the label of each wire to the current
                    it carries. The labels must be the keys in the wires
                    dictionary and the current should be considered positive if
                    it is flowing from the starting junction to the ending
                    junction as specified in the wires dictionary.
    """
    raise NotImplementedError

def findMaximumDeviationJunction(junctions, wires, resistances, voltages, currents):
    """
        Note that this part is completely optional and would not contribute to your grade.
        
        Given:
            junctions:  A set of junctions. Each junction is labeled by a
                        string or a tuple.
            wires:      A dictionary mapping a unique wire ID (a string or tuple)
                        to a tuple of two elements representing the starting and
                        ending junctions of the wire respectively. The set of
                        wire IDs is disjoint from the set of junction labels.
                        Note that although electricity can flow in either
                        direction, each wire between a pair of junctions will
                        appear exactly once in the list. Moreover, the starting
                        and ending junctions are distinct.
            resistances:A dictionary mapping each unique wire ID to a numeric
                        value representing the magnitude of the resistance of
                        the wire in Ohms. This dictionary has the same set of
                        keys as the wires dictionary.
            voltages:   A dictionary mapping each unique wire ID to a numeric
                        value representing the voltage (EMF or potential
                        difference) of the battery connected along the wire in
                        Volts. The positive terminal of the battery is next to
                        the ending junction (as defined in the wires dictionary)
                        if the voltage is positive whereas it is next to the
                        starting junction otherwise. This dictionary also has 
                        the same set of keys as the wires dictionary.
            currents:   A dictionary mapping each unique wire ID to a numeric
                        value representing the indicated current flowing along
                        the wire. The format is identical to that of the output 
                        of the previous function. Note that the values will not
                        necessarily be correct.
        Return:
            result: A junction with the maximum deviation from current
                    conservation. Note that any junction with maximal deviation
                    will be accepted.
    """
    raise NotImplementedError

def findMaximumDeviationLoop(junctions, wires, resistances, voltages, currents):
    """
        Note that this part is completely optional and would not contribute to your grade.
        
        Given:
            junctions:  A set of junctions. Each junction is labeled by a string
                        or a tuple.
            wires:      A dictionary mapping a unique wire ID (a string or tuple)
                        to a tuple of two elements representing the starting and
                        ending junctions of the wire respectively. The set of
                        wire IDs is disjoint from the set of junction labels.
                        Note that although electricity can flow in either
                        directions, each wire between a pair of junctions will
                        appear exactly once in the list. Moreover, the starting
                        and ending junctions are distinct.
            resistances:A dictionary mapping each unique wire ID to a numeric
                        value representing the magnitude of the resistance of 
                        the wire in Ohms. This dictionary has the same set of
                        keys as the wires dictionary.
            voltages:   A dictionary mapping each unique wire ID to a numeric
                        value representing the voltage (EMF or potential
                        difference) of the battery connected along the wire in
                        Volts. The positive terminal of the battery is next to
                        the ending junction (as defined in the wires dictionary)
                        if the voltage is positive whereas it is next to the 
                        starting junction otherwise. This dictionary also has
                        the same set of keys as the wires dictionary.
            currents:   A dictionary mapping each unique wire ID to a numeric
                        value representing the indicated current flowing along
                        the wire. The format is identical to that of the output
                        of the previous function. Note that the values will not
                        necessarily be correct.
        Return:
            result: A list of wires IDs representing the edges along a loop with
                    maximal (additive) deviation from Kirchoff's loop law.
                    The wires should be in order along the cycle but the
                    starting node and the direction may be arbitrary.
    """
    raise NotImplementedError

if __name__ == '__main__':
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used for testing.
    
    variables = {'x', 'y', 'z', 'w'}
    equations = [{'w': 2, 'x': 3, 1: -5},
                     {'y': 4, 'z': 7, 1: -5},
                     {'w': 1, 'y': -1},
                     {'w': 4, 'z': 2, 1: -6}]
    print(solveLinear(variables, equations))

    # var = 'x'
    # equation = {'x': 1, 'y': 1, 1: -3}
    # subEq = {'x': 1, 'y': -1, 1: 1}
    # print(substituteEquation(equation, var, subEq))
    