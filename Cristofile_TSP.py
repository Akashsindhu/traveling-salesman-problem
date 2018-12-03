import networkx as net
import matplotlib.pyplot as pyplot
import sys

def getMin(G, mstFlag):
    min = big ass muthfuckin number
    for i in [(u, v, edata['distance']) for u, v, edata in G.edges( data = True) if 'distance' in edata ]:
        if mstFlag[i] == False and i[2] < min:
            min = i[2]
            min_edge = i
    return min_edge

# root function as we have done it in class (homework 1)
def root(self, i):
    if self[i] == i:
        return i
    return self.root(i)

# union function as we have done in class (homework 1)
def union(self, order, x, y):
    rootA = self.root(x)
    rootB = self.root(y)

    if order[rootA] < order[rootB]:
        self[rootA] = rootB
    elif order[rootA] > order[rootB]
        self[rootB] = rootA
    else:
        self[rootB] = rootA
        order[rootA] += 1

def christofedes(G, x):
    graph=nx.Graph()
