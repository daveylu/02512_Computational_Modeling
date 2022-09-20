# the following three functions are taken from https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#printing
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

def intersect_mst(n, G):
    T = []

    membership = dict() #how we will check for equal sets
    for i in range(n):
        membership[i] = []
 
    edges = []
    for i in range(n):
        for j in range(i + 1, n): #looks at top half only, no need to do others
            edges.append([G[i][j], i, j])
    edges.sort()
    return edges

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