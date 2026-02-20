import numpy as np
import ast

def bul_umn(M1, M2):
    A = np.array(M1)
    B = np.array(M2)
    C = (A @ B > 0).astype(int)
    print(C)

def bul_slozh(M1, M2):
    A = np.array(M1)
    B = np.array(M2)
    C = (A + B > 0).astype(int)
    print(C)

M1 = ast.literal_eval(input())
M2 = ast.literal_eval(input())

bul_slozh(M1, M2)
