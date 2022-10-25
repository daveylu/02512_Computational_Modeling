import sys
import random
import math
import matplotlib.pyplot as plt


# the following function is taken from:
# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
# assists with opening files
def read_file(path):
    with open(path, "rt") as f:
        return f.read()

def model(r, d, dt, dx, k1, k2, X, total_T):
    steps = total_T // dt
    points = (X // dx) + 1
    times = []
    A_avgs = []
    B_avgs = []

    #X[i] contains the concentration of X at point i in the tube
    A = [0 for i in range(points)]
    B = [0 for i in range(points)]
    
    #Dirichlet boundary conditions
    A[0] = 1    
    A[-1] = 1
    B[0] = 0
    B[-1] = 0

    for step in range(steps):
        t = step * dt
        z1 = random.normalvariate(0, 1)
        z2 = random.normalvariate(0, 1)
        for i in range(1, points - 1):
            A_part1 = A[i] + dt * d * ((A[i + 1] + A[i - 1] - 2*A[i]) / dx**2)
            A_part2 = 4 * dt * (k2 * B[i] - k1 * A[i]**4)
            A_part3 = 2 * r * math.sqrt(dt) * (z2 * math.sqrt(k2 * B[i]) - z1 * math.sqrt(k1 * A[i]**4))
            B_part1 = B[i] + dt * (k1 * A[i]**4 - k2 * B[i])
            B_part2 = r * math.sqrt(dt) * (-z2 * math.sqrt(k2 * B[i]) + z1 * math.sqrt(k1 * A[i]**4))

            A[i] = A_part1 + A_part2 + A_part3
            B[i] = B_part1 + B_part2
        A_avg = sum(A) / len(A)
        B_avg = sum(B) / len(B)
        print(t, A_avg, B_avg)
        times.append(t)
        A_avgs.append(A_avg)
        B_avgs.append(B_avg)
    return times, A_avgs, B_avgs



def main():
    input_file = sys.argv[-1]
    input = read_file(input_file).splitlines()
    r = input[0]
    d = input[1]
    dt = input[2]
    dx = input[3]
    X = 2
    k1 = 1
    k2 = 1
    total_T = input[4]
    times, A_avgs, B_avgs = model(r, d, dt, dx, k1, k2, X, total_T)
    plt.plot(times, A_avgs)
    plt.plot(times, B_avgs)
    plt.xlabel("Times")
    plt.ylabel("Average Concentrations")
    plt.show()
    return