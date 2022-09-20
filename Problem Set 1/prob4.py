# the following three functions are taken from:
# https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#printing
def repr2dList(L):
    if (L == []): return '[]'
    output = [ ]
    rows = len(L)
    cols = max([len(L[row]) for row in range(rows)])
    M = [['']*cols for row in range(rows)]
    for row in range(rows):
        for col in range(len(L[row])):
            M[row][col] = repr(L[row][col])
    colWidths = [0] * cols
    for col in range(cols):
        colWidths[col] = max([len(M[row][col]) for row in range(rows)])
    output.append('[\n')
    for row in range(rows):
        output.append(' [ ')
        for col in range(cols):
            if (col > 0):
                output.append(', ' if col < len(L[row]) else '  ')
            output.append(M[row][col].rjust(colWidths[col]))
        output.append((' ],' if row < rows-1 else ' ]') + '\n')
    output.append(']')
    return ''.join(output)

def print2dList(L):
    print(repr2dList(L))

def read_file(path):
    with open(path, "rt") as f:
        return f.read()


#edge format: [weight, start vertex, stop vertex]
def intersect_mst_helper(graph_T, T, membership, edge):
    u, v = edge[1], edge[2]
    if(membership[u] != membership[v]):
        membership[v] += membership[u]
        membership[u] = membership[v]
        T.append((u, v))
        graph_T[u][v] = 1
        graph_T[v][u] = 1
    return

def find_cycles(n, graph_T, T, same_weight_edges):
    remove = []
    for edge in range(same_weight_edges):
        u, v = edge[1], edge[2]
        #remove the edge we're looking at from graph_T and then DFS from u to v
    return
    

def intersect_mst(n, G):
    T = []
    graph_T = [([0] * n) for i in range(n)]
    membership = dict() #how we will check for equal sets
    for i in range(n):
        membership[i] = [i]
 
    edges = []
    for i in range(n):
        for j in range(i + 1, n): #looks at top half only, no need to do others
            weight = G[i][j]
            if(weight != 0):
                edges.append([weight, i, j])
    edges.sort()

    same_weight_edges = []
    for i in range(len(edges)):
        if(i != (len(edges) - 1) and edges[i][0] == edges[i + 1][0]): #weight of the next edge is the same as the previous
            intersect_mst_helper(graph_T, T, membership, edges[i])
            same_weight_edges.append(edges[i])
        else:
            intersect_mst_helper(graph_T, T, membership, edges[i])
            same_weight_edges.append(edges[i])
            find_cycles(n, graph_T, T, same_weight_edges)
    return T

def main(input_file):
    input = read_file(input_file).splitlines()
    n = int(input[0])

    for i in range(1, n + 1):
        input[i] = input[i].split("  ")
    G = [([0] * n) for i in range(n)]

    for i in range(1, n + 1):
        for j in range(n):
            G[i - 1][j] = int(input[i][j])
    return intersect_mst(n, G)

print(main("sample1.txt"))