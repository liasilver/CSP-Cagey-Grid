# =============================
# Student Names: Lia Silver, Sydney Shereck, Mayy Mounib
# Group ID: 1
# Date: Feb 5th, 2023
# =============================
# CISC 352 - W23
# cagey_csp.py
# desc: two CSP models which use binary not-equal and n-ary all different to solve cagey grid problems.  
#

from itertools import permutations
from cspbase import *

def binary_ne_grid(cagey_grid):
  # A model of a Cagey grid (without cage constraints) built using only binary not-equal constraints for both the row and column constraints. Takes a cagey grid and returns a CSP object and a list of Variable objects representing the board. 
  
    size = cagey_grid[0] #get size of grid from first element of input list
    values = []
    gridVariables = [] #empty queue to store variables
    gridVariablesList = [] #same as gridVariables as type list

    
    for i in range(size):
        # Initialize a list to store variables for each row
        vals = values
        for j in range(size):
            # Get domain for each variable in the grid 
            domain = [k for k in range(1, size + 1)]
            # Create variable for each cell 
            v = Variable("{}{}".format(i, j), domain)
            vals.append(v)
        gridVariables.append(vals)

    constraints = []
    tuples = []

    #turn queue in to list type and create csp with this varaible list
    gridVariablesList = [v for r in gridVariables for v in r]
    csp = CSP("binary_ne_grid", gridVariablesList)

    #create a list of all possible combinations of variables
    possibleTuples = [(i, j) for i in range(1, size + 1) for j in range(1, size + 1) if i != j]
    tuples = possibleTuples
    for i in range(size):
        for j in range(size):
            for k in range(j + 1, size):
                col = [gridVariables[j][i], gridVariables[k][i]]
                constraint = Constraint("c{}{}{}".format(i, j, k), col)
                constraint.add_satisfying_tuples(tuples)
                constraints.append(constraint)
                row = [gridVariables[i][j], gridVariables[i][k]]
                constraint = Constraint("r{}{}{}".format(i, j, k), row)
                constraint.add_satisfying_tuples(tuples)
                constraints.append(constraint)
    for constraint in constraints:
        csp.add_constraint(constraint)
    return csp, gridVariables


def nary_ad_grid(cagey_grid):
  # A model of a Cagey grid (without cage constraints) built using only n-ary all-different constraints for both the row and column constraints. Takes a cagey grid and returns a CSP object and a list of Variable objects representing the board. 
  
    n = cagey_grid[0] #grid size
    row = []
    col = []
    variables = []
    tuples = []
    csp = CSP("nary_ad_grid")

  #create n permutation constraints
    permutation_list = list(range(1, n + 1))
    for i in permutations(permutation_list, n):
        tuples.append(i)

    for i in range(1, n + 1):
        row.append([])
        col.append([])

    for i in range(1, n + 1):
        #create variables
        y_variables = []
        for j in range(1, n + 1):
            domain = list(range(1, n + 1))
            new_var = Variable("%d%d" % (i, j), domain)
            row[i - 1].append(new_var)
            col[j - 1].append(new_var)
            csp.add_var(new_var)
            y_variables.append(new_var)
        variables.append(y_variables)
    
    for i in range(1, n + 1):
        #create col & row n-ary constraints
        cons = Constraint("r%d" % i, row[i - 1])
        cons.add_satisfying_tuples(tuples)
        csp.add_constraint(cons)
        cons = Constraint("c%d" % i, col[i - 1])
        cons.add_satisfying_tuples(tuples)
        csp.add_constraint(cons)

    return csp, variables

def cagey_csp_model(cagey_grid):
  pass

