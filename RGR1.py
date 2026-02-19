import numpy as np
import ast

#1.Дизъюнкция
def bul_umn(M1, M2):
    A = np.array(M1)
    B = np.array(M2)
    C = (A @ B > 0).astype(int)
    print(C)

#2.Транспонирование
def transp(M1):
    A = np.array(M1)
    np.transpose(A)
    print(A)


#3.Инвертирование
def invert(M1):
    A = np.array(M1)
    np.linalg.inv(A)
    print(A)

#4.Вычитание
def vichit(M1, M2):
    A = np.array(M1)
    B = np.array(M2)
    C = np.subtract(A, B)
    print(C)

#5.Умножение
def umnozh(M1, M2):
    A = np.array(M1)
    B = np.array(M2)
    C = A @ B
    print(C)


M1 = ast.literal_eval(input())
M2 = ast.literal_eval(input())
