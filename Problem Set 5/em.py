import sys

# the following function is taken from:
# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
# assists with opening files
def read_file(path):
    with open(path, "rt") as f:
        return f.read()

def e_step(H, B, Y, f):
    for i in range(len(B)):
        if(B[i] == 0):
            Y[i] = 0
        else:
            Y[i] = (H[i] * f) / (1 - (1 - f)**H[i])
    return Y

def m_step(H, Y):
    return sum(Y) / sum(H)

def em(H, B, Y, f, r):
    for i in range(r):
        Y = e_step(H, B, Y, f)
        f = m_step(H, Y)
    return f

def main():
    input_file = sys.argv[-1]
    input = read_file(input_file).splitlines()
    f = float(input[0])
    r = int(input[1])
    H = []
    B = []
    Y = []
    for i in range(3, len(input)):
        h, b = input[i].split(" ")
        H.append(int(h))
        B.append(int(b))
        Y.append(0)
    
    f = em(H, B, Y, f, r)
    print(f"f = {f}")
    return

main()
