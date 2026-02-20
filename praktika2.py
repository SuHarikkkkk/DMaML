from scipy.sparse import csr_array
from scipy.sparse.csgraph import floyd_warshall
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def bul_umn(M1, M2):
    A = np.array(M1)
    B = np.array(M2)
    C = (A @ B > 0).astype(int)
    return C

def bul_slozh(M1, M2):
    A = np.array(M1)
    B = np.array(M2)
    C = (A + B > 0).astype(int)
    return C

G1=nx.DiGraph(directed=True)
G2=nx.DiGraph(directed=True)


G1.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
r1=[(1,1),(1,3),(1,7),(2,4),(4,3),(3,4),(4,7),(5,5),(5,7),(3,1)]
r2=[(3,2),(7,4),(4,3),(4,4),(4,5),(5,7),(7,1),(7,2),(1,2),(2,7)]

G1.add_edges_from(r1)
G2.add_edges_from(r2)

#nx.draw(G1, with_labels=True, node_color='lightblue')
#plt.show()

#nx.draw(G2, with_labels=True, node_color='lightblue')
#plt.show()

n = 7
B = np.zeros((n, n))
C = np.zeros((n, n))

for t in r1:
    B[t[0] - 1][t[1] - 1] = 1

for t in r2:
    C[t[0] - 1][t[1] - 1] = 1

N3 = bul_umn(B, C)
graph3 = N3
graph = csr_array(graph3)
print(graph3)

print('fffffffffffffffffffffff')

N4 = bul_slozh(B, C)
graph4 = N4
graph4 = csr_array(graph4)
print(graph4)

N5 = B*C
graph5 = N5
graph5 = csr_array(graph5)
print(graph5)
