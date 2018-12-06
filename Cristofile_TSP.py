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

def generateGraph():
    # Instantiate an empty Graph with no Vertices(Nodes) and Edges
    G = net.Graph()
    # Assign a variable the contents of the Text File
    graph_specs = open('graph_5vert.txt')
    # typecast data in Text_File from string into int
    file_oneline = int(graph_specs.readline())
    # list if edge weights matrix
    weightMatrix = []
    # variable for each line from the text file (string)
    file_oneline2 = graph_specs.readline() # string value
    # val = each string line in text file
    for val in range(file_oneline):
        # typecast indivual string edge_weight values into integers
        oneline_file_values_list = map(int,file_oneline2.split())
        # append edge_weight values to the Matrix rows
        weightMatrix.append(oneline_file_values_list)

    # Adds edges along with their weights to the graph
    for row in range(file_oneline):
        for column in range(file_oneline)[row:]:
            # if the edge_weight between two nodes is greater than 0
            if weightMatrix[row][column] > 0:
                # add the edge_weight to [row]x[column] described path
                G.add_edge(row, column, distance = weightMatrix[row][column])
    return G # return a Graph

def sketchGraph(G, color):
    # returns a Dictionary of positions keyed by node
    node_position = net.spring_layout(G)
    # draws the graph using matplotlib
    net.draw(G,node_position,with_labels = True, edge_color = color)
    # returns a Dictionary of Attributes keyed by edge. Multi(di)graph, Keys are 3-tuples(u,v,key)
    edge_labels = net.get_edge_attributes(G,'distance')
    # returns a Dictionary of labels keyed on the Edges
    net.draw_networkx_edge_labels(G,node_position,edge_labels = edge_labels)

    return node_position
