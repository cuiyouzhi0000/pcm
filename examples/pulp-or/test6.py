#!/usr/bin/env python
# @(#) $Jeannot: test1.py,v 1.11 2005/01/06 21:22:39 js Exp $
# Copywrite 2007 Stuart Mitchell
# Columnwise modelling

# Import PuLP modeler functions
from pulp import *

# A new LP problem
prob = Prob( "test6", MIN )

# objective
obj = LpConstraintVar( "obj" )

# constraints

a = LpConstraintVar( "Ca", DVarConstraintLE, 5 )

b = LpConstraintVar( "Cb", DVarConstraintGE, 10 )

c = LpConstraintVar( "Cc", DVarConstraintEQ, 7 )

prob.setObjective( obj )
prob += a
prob += b
prob += c

# Variables
# 0 <= x <= 4
x = DVar( "x", 0, 4, DVarC, obj + a + b )
# -1 <= y <= 1
y = DVar( "y", -1, 1, DVarC, 4 * obj + a - c )
# 0 <= z
z = DVar( "z", 0, None, DVarC, 9 * obj + b + c )
# Use None for +/- Infinity, i.e. z <= 0 -> DVar("z", None, 0)


# Write the problem as an LP file
prob.writeLP( "test6.lp" )

# Solve the problem using the default solver
prob.solve()
# Use prob.solve(GLPK()) instead to choose GLPK as the solver
# Use GLPK(msg = 0) to suppress GLPK messages
# If GLPK is not in your path and you lack the pulpGLPK module,
# replace GLPK() with GLPK("/path/")
# Where /path/ is the path to glpsol (excluding glpsol itself).
# If you want to use CPLEX, use CPLEX() instead of GLPK().
# If you want to use XPRESS, use XPRESS() instead of GLPK().
# If you want to use COIN, use COIN() instead of GLPK(). In this last case,
# two paths may be provided (one to clp, one to cbc).

# Print the status of the solved LP
print "Status:", LpStatus[prob.status]

# Print the value of the variables at the optimum
for v in prob.variables():
    print v.name, "=", v.varValue

# Print the value of the objective
print "objective=", value( prob.objective )