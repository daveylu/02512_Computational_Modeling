from numpy import random
from matplotlib import pyplot as plt

def passive_model(x1, x2, init_S, init_I, init_D, N, T):
    all_infected = 0
    for i in range(T):
        t = 0
        S = init_S
        I = init_I
        D = init_D
        if(i == 0):
            points_t = [0]
            points_S = [S]
            points_I = [I]
            points_D = [D]
        while(I > 0 and S > 0):
            t_i = random.exponential((x1 * I * S) / N)
            t_d = random.exponential(x2 * I)
            if(t_i < t_d):
                S -= 1
                I += 1
                t += t_i
            else:
                I -= 1
                D += 1
                t += t_d

            if(i == 0):
                points_t.append(t)
                points_S.append(S)
                points_I.append(I)
                points_D.append(D)
            
        if(i == 0):
            points = [points_t, points_S, points_I, points_D]
        if(S == 0):
            all_infected += 1


    return all_infected / T, points

    

def active_model(x1, x2, x3, init_S, init_I, init_D, N, T):
    all_infected = 0
    for i in range(T):
        t = 0
        S = init_S
        I = init_I
        D = init_D
        if(i == 0):
            points_t = [0]
            points_S = [S]
            points_I = [I]
            points_D = [D]
        while(I > 0 and S > 0):
            t_i = random.exponential((x1 * I * S) / N)
            t_d = random.exponential(x2 * I)
            t_k = random.exponential((x3 * I * S) / N)
            if(t_i < t_d and t_i < t_k):
                S -= 1
                I += 1
                t += t_i
            else:
                I -= 1
                D += 1
                t += t_d
            if(i == 0):
                points_t.append(t)
                points_S.append(S)
                points_I.append(I)
                points_D.append(D)

        if(i == 0):
            points = [points_t, points_S, points_I, points_D]
        if(S == 0): all_infected += 1

    return all_infected / T, points

def wrapper(x1, x2, x3, N, m, T):
    S = N - m
    I = m
    D = 0
    passive_result, passive_points = passive_model(x1, x2, S, I, D, N, T)
    active_result, active_points = active_model(x1, x2, x3, S, I, D, N, T)
    print(f"x2 = {x2}")
    print(f"Passive Model - fraction of all infected: {passive_result}")

    plt.plot(passive_points[0], passive_points[1], label = "Susceptible")
    plt.plot(passive_points[0], passive_points[2], label = "Infected")
    plt.plot(passive_points[0], passive_points[3], label = "Dead")
    plt.title(fr"Not fighting back: $\lambda_2 = ${x2}")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.legend()
    plt.show()

    print(f"Active Model - fraction of all infected: {active_result}")
    plt.plot(active_points[0], active_points[1], label = "Susceptible")
    plt.plot(active_points[0], active_points[2], label = "Infected")
    plt.plot(active_points[0], active_points[3], label = "Dead")
    plt.title(fr"Fighting back: $\lambda_2 = ${x2}")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.legend()
    plt.show()

def main():
    wrapper(1.5, 0.001, 1, 10000, 100, 100)
    wrapper(1.5, 0.01, 1, 10000, 100, 100)
    wrapper(1.5, 0.1, 1, 10000, 100, 100)
    wrapper(1.5, 1, 1, 10000, 100, 100)
    wrapper(1.5, 10, 1, 10000, 100, 100)
    wrapper(1.5, 100, 1, 10000, 100, 100)

main()