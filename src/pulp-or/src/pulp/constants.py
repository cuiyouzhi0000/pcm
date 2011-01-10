# PuLP : Python LP Modeler
# Version 1.20

# Copyright (c) 2002-2005, Jean-Sebastien Roy (js@jeannot.org)
# Modifications Copyright (c) 2007- Stuart Anthony Mitchell (s.mitchell@auckland.ac.nz)
# $Id:constants.py 1791 2008-04-23 22:54:34Z smit023 $

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

"""
This file contains the constant definitions for PuLP
Note that hopefully these will be changed into something more pythonic
"""

EPS = 1e-7

# variable categories
DVarC = "Continuous"
DVarI = "Integer"
DVarB = "Binary"
DVarType = {DVarC: "Continuous", DVarI: "Integer",
                DVarB: "Binary"}

# objective sense
MIN = 1
MAX = -1
Sense = {MAX:"Maximize", MIN:"Minimize"}

# problem status
LpStatusNotSolved = 0
LpStatusOptimal = 1
LpStatusInfeasible = -1
LpStatusUnbounded = -2
LpStatusUndefined = -3
LpStatus = { LpStatusNotSolved:"Not Solved",
    LpStatusOptimal:"Optimal",
    LpStatusInfeasible:"Infeasible",
    LpStatusUnbounded:"Unbounded",
    LpStatusUndefined:"Undefined",
    }

# constraint sense
DVarConstraintLE = -1
DVarConstraintEQ = 0
DVarConstraintGE = 1
DVarConstraintSenses = {DVarConstraintEQ:"=", DVarConstraintLE:"<=", DVarConstraintGE:">="}

# LP line size
DVarCplexLPLineSize = 78

def isiterable( obj ):
    try: obj = iter( obj )
    except: return False
    else: return True