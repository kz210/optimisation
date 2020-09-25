import numpy as np
from scipy.optimize import minimize

"""
obj func: min x1*x4*(x1+x2+x3)+x3
s.t. x1*x2*x3*x4 >=25
     sum(xi^2)=40
     1<=xi<=5
     x0=(1,5,5,1) initial guess
"""
def objective(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return x1*x4*(x1+x2+x3)+x3

def constraint1(x):
    return x[0]*x[1]*x[2]*x[3] - 25.0

def constraint2(x):
    sum_sqs = 40
    for element in x:
        sum_sqs -= element**2
    return sum_sqs

x0 = [1,5,5,1]
print(objective(x0))
b = (1.0, 5.0)
bnds = (b,b,b,b)
cons1 = {'type':'ineq','fun':constraint1}
cons2 = {'type':'eq','fun':constraint2}
cons =[cons1,cons2]

sol = minimize(objective,x0,method = 'SLSQP', \
    bounds = bnds, constraints=cons)
print(sol.x)
print(sol.fun)