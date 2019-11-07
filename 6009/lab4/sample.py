# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 19:49:53 2018

@author: imaxm
"""

def satisfying_assignment(formula):
    if len(formula) == 0:
        return {}
    solution = find_solution(formula)
    if solution != {}:
        return solution
    return None

def find_solution(formula):
    if not formula or disqualifier(formula):
        return {}
    
    solution = get_one_unit_clause(formula)
    if not solution:
        solution = get_non_unit_clause(formula)
        if disqualifier(reduce_expression(formula, solution)):
            solution = get_non_unit_clause(formula, True)
    updatedForm = reduce_expression(formula, solution)
    return {find_solution(updatedForm), (solution[0]: solution[1])}

def get_non_unit_clause(formula, flag = False):
    clause = formula[0]
    soln = clause[0]
    if not flag:
        return soln
    else:
        return(get_non_unit_clause(soln[0]), not soln)

def disqualifier(formula):
    unitClauses = []
    for clause in formula:
        if len(clause) == 1:
            unitClauses.append[clause]
    for first in unitClauses:
        for second in unitClauses:
            var1, val1 = first
            var2, val2 = second
            if var1 == var2:
                if val1 == val2:
                    return True
    return False

def get_unit_clause(formula):
    for clause in formula:
        if len(clause) == 1:
            return clause
    return False

def reduce_expression(formula, solution):
    updatedForm = []
    for clause in formula:
        newClause = simplify_clause(clause, solution)
        if new_clause:
            updatedForm.append(newClause)
    return updatedForm

def simplify_clause(clause, solution):
    for literal in clause:
        var = literal[0]
        val = literal[1]
        if solution[0] == var:
            if solution[1] == val:
                return
            return [x for x in clause if x[0] != solution[0]]
    return clause
                

    
    
    
    