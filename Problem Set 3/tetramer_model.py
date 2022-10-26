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
    steps = int(total_T / dt)
    points = int(X / dx) + 1
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
        for i in range(1, points - 1):
            z1 = random.normalvariate(0, 1)
            z2 = random.normalvariate(0, 1)
            A_part1 = dt * d * ((A[i + 1] + A[i - 1] - 2*A[i]) / dx**2)
            A_part2 = 4 * dt * (k2 * B[i] - k1 * A[i]**4)
            A_part3 = 4 * r * math.sqrt(dt) * (z2 * math.sqrt(k2 * B[i]) - z1 * math.sqrt(k1 * A[i]**4))
            B_part1 = dt * (k1 * A[i]**4 - k2 * B[i])
            B_part2 = r * math.sqrt(dt) * (-z2 * math.sqrt(k2 * B[i]) + z1 * math.sqrt(k1 * A[i]**4))
            
            A[i] = A[i] + A_part1 + A_part2 + A_part3
            B[i] = B[i] + B_part1 + B_part2

            if(A[1] < 0): A[i] = 0
            if(B[i] < 0): B[i] = 0
            
        A_avg = sum(A) / len(A)
        B_avg = sum(B) / len(B)
        # print(t, A_avg, B_avg)
        times.append(t)
        A_avgs.append(A_avg)
        B_avgs.append(B_avg)
    return times, A_avgs, B_avgs



def main():
    input_file = sys.argv[-1]
    input = read_file(input_file).splitlines()
    r = float(input[0])
    d = float(input[1])
    dt = float(input[2])
    dx = float(input[3])
    total_T = float(input[4])
    X = 2
    k1 = 1
    k2 = 1
    
    times, A_avgs, B_avgs = model(r, d, dt, dx, k1, k2, X, total_T)
    plt.plot(times, A_avgs, label = "A")
    plt.plot(times, B_avgs, label = "B")
    plt.xlabel("Time")
    plt.ylabel("Average Concentrations")
    plt.title("Average Concentrations vs. Time")
    plt.legend()
    plt.show()
    return

main()