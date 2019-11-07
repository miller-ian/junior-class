"""6.009 Lab 5 -- Boolean satisfiability solving"""

import sys
sys.setrecursionlimit(10000)
#NO ADDITIONAL IMPORTS

def satisfying_assignment(formula):
    """
    Find a satisfying assignment for a given CNF formula.
    Returns that assignment if one exists, or None otherwise.

    >>> satisfying_assignment([])
    {}
    >>> x = satisfying_assignment([[('a', True), ('b', False), ('c', True)]])
    >>> x.get('a', None) is True or x.get('b', None) is False or x.get('c', None) is True
    True
    >>> satisfying_assignment([[('a', True)], [('a', False)]])
    """
    if len(formula) == 0:
        return {}
    solution = find_solution(formula)
    if solution != {}:
        return solution
    return None

def find_solution(formula):
    """
    Finds a potential solution depending on whether a future clause contradicts a previous one. Looks for unit
    clauses first, then moves onto non-unit clauses.
    """
    #if formula is empty or if there is a contradiction between clauses
    if not formula or disqualifier(formula):
        return {}
    
    solution = get_one_unit_clause(formula)
    #if there are no unit clauses, move on to non-unit clauses
    if not solution:
        solution = get_non_unit_clause(formula)
        #if there are contradictions with literals on non-unit clauses, backtrack, get rid of that contradicting literal, and try again
        if disqualifier(reduce_expression(formula, solution)):
            solution = get_non_unit_clause(formula, True)
    updatedForm = reduce_expression(formula, solution)
    #double asterisks allow any number of keywords to be passed as an argument
    return {**find_solution(updatedForm), **{solution[0]: solution[1]}}

def get_non_unit_clause(formula, flag = False):
    #finds a multi-literal clause and has the ability to return an inverted version of the literal or just the literal itself
    clause = formula[0]
    literal = clause[0]
    soln = literal
    return soln if not flag else (soln[0], not soln)

def disqualifier(formula):
    #compiles a list of unit clauses
    unitClauses = [clause[0] for clause in formula if len(clause)==1]
    for c1 in unitClauses:
        for c2 in unitClauses:
            #if two copies of the same variable are equal to different values, there is a contradiction
            var1, val1 = c1
            var2, val2 = c2
            if var1 == var2:
                if val1 != val2:
                    return True
    return False

def get_one_unit_clause(formula):
    #returns the first unit clause in the formula
    for clause in formula:
        if len(clause) == 1:
            return clause
    return False

def simplify_clause(clause, solution):
    #once a clause is satisfied, move on to the next clause
    #not necessary to check all literals
    for literal in clause:
        var = literal[0]
        val = literal[1]
        if solution[0] == var:
            if solution[1] == val:
                return
            return [x for x in clause if x[0] != solution[0]]
    return clause

def reduce_expression(formula, solution):
    #using simplified clauses, reduce the expression as a whole
    updatedForm = []
    for clause in formula:
        newClause = simplify_clause(clause, solution)
        if newClause:
            updatedForm.append(newClause)
    return updatedForm
                


def boolify_scheduling_problem(student_preferences, session_capacities):
    """
    Convert a quiz-room-scheduling problem into a Boolean formula.

    student_preferences: a dictionary mapping a student name (string) to a set
                         of session names (strings) that work for that student
    session_capacities: a dictionary mapping each session name to a positive
                        integer for how many students can fit in that session

    Returns: a CNF formula encoding the scheduling problem, as per the
             lab write-up
    We assume no student or session names contain underscores.
    """
    #first constraint for assignment
    #clause will consist of name_preference = True (or)
    cnf = []
    names = student_preferences.keys()
    for name in names:
        clause = []
        preferences = student_preferences[name]
        for preference in preferences:
            literal = (str(name) + '_' + str(preference)), 'True'
            clause.append(literal)
        cnf.append(clause)
    #concatenate other 2 constraints, as detailed by the helper functions below
    cnf += one_session(student_preferences, session_capacities)
    cnf += oversubscribed(student_preferences, session_capacities)
    return cnf 

def one_session(student_preferences, session_capacities):
    #makes sure every student is only in 1 session
    cnf = []
    locations = session_capacities.keys()
    names = student_preferences.keys()
    locationList = []
    for i in locations:
        locationList.append(i)
    #taking pairs of locations for each student, one must be false
    for name in names:
        firstLoc = ''
        secondLoc = ''

        for i in range(len(locationList)-1):
            iterate = i + 1
            for j in locationList[iterate:]:
                clause = []
                firstLoc = locationList[i]
                secondLoc = j
                firstLiteral = (str(name) + '_' + str(firstLoc)), 'False'
                secondLiteral = (str(name) + '_' + str(secondLoc)), 'False'
                clause.append(firstLiteral)
                clause.append(secondLiteral)
                cnf.append(clause)

    return cnf

def oversubscribed(student_preferences, session_capacities):
    #makes sure no session has more students than it can hold
    cnf = []
    locationsToCheck = []
    numStudents = len(student_preferences.keys())
    studentList = []
    for i in student_preferences.keys():
        studentList.append(i)
    for i in session_capacities.keys():
        if session_capacities[i] < numStudents:
            locationsToCheck.append(i)
    #for each location, take every possible combination of (session_capacity + 1) students, set all to False
    for location in locationsToCheck:
        numSeats = session_capacities[location]
        select = numSeats + 1
        combinations = combo_return(studentList, select)
        for combo in combinations:
            clause = []
            for name in combo:
                name = name + '_' + location
                literal = name, False
                clause.append(literal)
            cnf.append(clause)
    return cnf

def get_combinations(elements, length):
    #use recursion to find all possible combos of a list of elements for a given length
    for i in range(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in get_combinations(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next

def combo_return(elemen, leng):
    return list(get_combinations(elemen, leng))


if __name__ == '__main__':
    import doctest
    _doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=_doctest_flags)
    