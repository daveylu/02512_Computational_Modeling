import sys
import math

def read_file(path):
    with open(path, "rt") as f:
        return f.read()

def passive_model(x1, x2, x3, S, I, D, N, T):
    all_infected = 0
    for i in range(T):
        t = 0
        while(I > 0):
            t_i = math.exp((x1 * I * S) / N)
            t_d = math.exp(x2 * I)
            if(t_i < t_d):
                S -= 1
                I += 1
                t += t_i
            else:
                I -= 1
                D += 1
                t += t_d
        if(S == 0): all_infected += 1
    return all_infected / T

    

def active_model(x1, x2, x3, S, I, D, N, T):
    all_infected = 0
    for i in range(T):
        t = 0
        while(I > 0):
            t_i = math.exp((x1 * I * S) / N)
            t_d = math.exp(x2 * I)
            t_k = math.exp((x3 * I * S) / N)
            if(t_i < t_d and t_i < t_k):
                S -= 1
                I += 1
                t += t_i
            else:
                I -= 1
                D += 1
                t += t_d
        if(S == 0): all_infected += 1
    return all_infected / T

def main():
    input_file = sys.argv[-1]
    input = read_file(input_file).splitlines()
    x1 = input[0]
    x2 = input[1]
    x3 = input[2]
    N = input[3]
    m = input[4]
    T = input[5]
    S = N - m
    I = N
    D = 0
    

