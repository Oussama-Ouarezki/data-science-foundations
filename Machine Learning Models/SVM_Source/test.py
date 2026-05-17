import sympy as sp
import numpy as np

A=[[1,0,-1],[0,1,-1],[-1,-1,2]]

A=sp.Matrix(A)
P,D=A.diagonalize()


p1=A[:,0].norm()
