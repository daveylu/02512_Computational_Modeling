import copy
import sys
"""
To run the code in a terminal, call: python prob4.py {insert file name here}

The input file must be in the EXACT SAME FORMAT as the sample files.
(number of vertices at the top, then the adjacency matrix, with numbers split
up by two spaces and each row split up with an enter)
"""
# the following function is taken from:
# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
# assists with opening files
def read_file(path):
    with open(path, "rt") as f:
        return f.read()

#performs DFS on a given graph.
#returns True if we can find the target from the start
def DFS(n, G, start, target):
    stack = [start]
    seen = []
    while(True):
        if(len(stack) == 0): return False
        v = stack.pop(0)
        seen.append(v)
        for i in range(n):
            if(G[v][i] > 0 and i not in seen):
                if(i == target): return True
                else: stack.insert(0, i)

#removes any edge from edges that are in a cycle of the graph
def remove_cycle_edges(n, graph_T, T, edges):
    remove = []
    for edge in edges:
        u, v = edge[1], edge[2]
        #remove the edge we're looking at from graph_T and then DFS from u to v
        temp_graph_T = copy.deepcopy(graph_T)
        temp_graph_T[u][v] = 0      #removing the edge that we are looking at
        temp_graph_T[v][u] = 0      #in order to use DFS to find a cycle
        if(DFS(n, temp_graph_T, u, v) == True):
        #if we find that the edge is part of a cycle: mark for deletion
            remove.append((u, v))
    for edge in remove: #delete marked edges
        if(edge in T):
            T.remove(edge)
            u, v = edge
            graph_T[u][v] = 0
            graph_T[v][u] = 0
    return

#update memberships
def update_membership(n, G, membership):
    for i in range(n):
        for j in range(i + 1, n):
            if(G[i][j] != 0):
                if(membership[i] != membership[j]): #prevents extra updating
                    membership[i] += membership[j]
                    for v in membership[i]:
                        membership[v] = membership[i]
    return

#adds an edge to the MST if they are not already connected
def insert_edge(graph_T, T, membership, edge):
    u, v = edge[1], edge[2]
    if(membership[u] != membership[v]):
        T.append((u, v))
        graph_T[u][v] = 1
        graph_T[v][u] = 1
    return

#primary function that finds the intersection MST
def intersect_mst(n, G):
    T = []
    graph_T = [([0] * n) for i in range(n)]
    membership = dict() #how we will check for equal sets
    for i in range(n):  #creation of the initial sets
        membership[i] = [i]

    edges = []
    for i in range(n):      #finding all of the edges and saving them to sort 
        for j in range(i + 1, n):   #looks at half only, no need for the others
            weight = G[i][j]
            if(weight != 0):
                edges.append([weight, i, j])
    edges.sort()

    same_weight_edges = [] #contains the edges we may need to delete later
    for i in range(len(edges)):
        if(i != (len(edges) - 1) and edges[i][0] == edges[i + 1][0]):
        #if weight of the next edge is the same as the previous
            insert_edge(graph_T, T, membership, edges[i])
            #not updating the memberships until we have added all edges of same weight
            same_weight_edges.append(edges[i])
        else:
            insert_edge(graph_T, T, membership, edges[i])
            update_membership(n, graph_T, membership)   #only update memberships now
            same_weight_edges.append(edges[i])
            remove_cycle_edges(n, graph_T, T, same_weight_edges) #the intersect part
            same_weight_edges = []
    return T

#files must be in the same format as the sample files
#returns the intersection MST as a list of edges
def main():
    input_file = sys.argv[-1]
    input = read_file(input_file).splitlines()
    
    n = int(input[0])                       
    for i in range(1, n + 1):               
        input[i] = input[i].split("  ")
    G = [([0] * n) for i in range(n)]       #this entire section is just
    for i in range(1, n + 1):               #parsing the file given
        for j in range(n):
            G[i - 1][j] = int(input[i][j])
    
    MST = intersect_mst(n, G)

    print(MST)
    return MST

main()