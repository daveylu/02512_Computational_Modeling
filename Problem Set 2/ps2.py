import numpy
import math
import sys

# the following function is taken from:
# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
# assists with opening files
def read_file(path):
    with open(path, "rt") as f:
        return f.read()

def dF_dA(A, k, n, points):
    sum = 0
    for i in range(n):
        part1 = (A * math.exp(-k * points[i][0])) - points[i][1]
        part2 = math.exp(-k * points[i][0])
        sum += part1 * part2
    return sum * 2

def dF_dk(A, k, n, points):
    sum = 0
    for i in range(n):
        part1 = (A * math.exp(-k * points[i][0])) - points[i][1]
        part2 = -A * points[i][0] * math.exp(-k * points[i][0])
        sum += part1 * part2
    return sum * 2

def newton_raphson(A0, k0, dA, dk, r, n, points):
    V = numpy.empty((2, 1))
    V[0][0] = A0
    V[1][0] = k0
    for i in range(r):
        A = V[0][0]
        k = V[1][0]

        gradient = numpy.empty((2, 1))
        gradient[0][0] = dF_dA(A, k, n, points)
        gradient[1][0] = dF_dk(A, k, n, points)

        H = numpy.empty((2, 2))

        calculation = dF_dA(A + dA, k, n, points) - gradient[0][0]
        H[0][0] = calculation / dA
        H[0][1] = calculation / dk

        calculation = dF_dk(A, k + dk, n, points) - gradient[1][0]
        H[1][0] = calculation / dA
        H[1][1] = calculation / dk

        determinant = (H[0][0] * H[1][1]) - (H[0][1] * H[1][0])
        y = numpy.matmul(H, gradient) * (1/determinant)

        V = V - y

    return [V[0][0], V[1][0]]


def main(input_file = None):
    if(input_file == None):
        input_file = sys.argv[-1]
    input = read_file(input_file).splitlines()

    A0 = float(input[0])
    k0 = float(input[1])
    dA = float(input[2])
    dk = float(input[3])
    r = int(input[4])
    n = int(input[5])

    points = list()
    for i in range(n):
        i += 6
        t, V, = input[i].split(" ")
        points.append([float(t), float(V)])
    
    result = newton_raphson(A0, k0, dA, dk, r, n, points)

    print(f"A is approximately: {result[0]}")
    print(f"k is approxiamtely: {result[1]}")

    return

main("test1.txt")