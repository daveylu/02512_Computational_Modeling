from numpy import random

def passive_model(x1, x2, S, I, D, N, T):
    all_infected = 0
    for i in range(T):
        t = 0
        while(I > 0):
            t_i = random.exponential((x1 * I * S) / N)
            t_d = random.exponential(x2 * I)
            if(t_i < t_d and S > 0):
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
            t_i = random.exponential((x1 * I * S) / N)
            t_d = random.exponential(x2 * I)
            t_k = random.exponential((x3 * I * S) / N)
            if(t_i < t_d and t_i < t_k and S > 0):
                S -= 1
                I += 1
                t += t_i
            else:
                I -= 1
                D += 1
                t += t_d
        if(S == 0): all_infected += 1
    return all_infected / T

def wrapper(x1, x2, x3, N, m, T):
    S = N - m
    I = N
    D = 0
    passive_result = passive_model(x1, x2, S, I, D, N, T)
    active_result = active_model(x1, x2, x3, S, I, D, N, T)
    print(f"x2 = {x2}")
    print(f"Passive Model - fraction of all infected: {passive_result}")
    print(f"Active Model - fraction of all infected: {active_result}")

def main():
    wrapper(1.5, 0.001, 1, 10000, 100, 100)
    wrapper(1.5, 0.01, 1, 10000, 100, 100)
    wrapper(1.5, 0.1, 1, 10000, 100, 100)
    wrapper(1.5, 1, 1, 10000, 100, 100)
    wrapper(1.5, 10, 1, 10000, 100, 100)
    wrapper(1.5, 100, 1, 10000, 100, 100)

main()