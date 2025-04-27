import numpy as np
import matplotlib.pyplot as plt
import random

 
def radioactive_decay(N0, decay_constant, time_end, dt):
    steps = int(time_end / dt)
    t = np.linspace(0, time_end, steps)
    N = np.zeros(steps)
    N[0] = N0

    for i in range(1, steps):
        noise = random.uniform(-0.05, 0.05)
        N[i] = N[i-1] - decay_constant * N[i-1] * dt + noise * N[i-1]

    return t, N

def radioactive_decay_analytical_solution(N0, decay_constant, t):
    N_exact = [N0 * np.exp(-decay_constant * time) for time in t]
    return N_exact

def plot_decay(t, N_numeric, N_exact, decay_constant):
    plt.figure(figsize=(8, 5))
    plt.plot(t, N_numeric, label='Numerical (Euler method)')
    plt.plot(t, N_exact, label='Analytical solution', linestyle='--')
    plt.xlabel('Time (t)') 
    plt.ylabel('Number of atoms (N)')
    plt.title(f'Radioactive Decay Simulation (λ = {decay_constant})')
    plt.legend()
    plt.grid(True)
    plt.savefig('plot.png')
    plt.show()

def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def main():
    print("Welcome to the Radioactive Decay Simulation!\n")

    N0 = ask_float("Enter the initial number of atoms (e.g., 1000): ")
    decay_constant = ask_float("Enter the decay constant λ (e.g., 0.05): ")
    time_end = ask_float("Enter the total simulation time (e.g., 100): ")
    dt = ask_float("Enter the time step (e.g., 0.1): ")

    t, N_numeric = radioactive_decay(N0, decay_constant, time_end, dt)
    N_exact = radioactive_decay_analytical_solution(N0, decay_constant, t)

    plot_decay(t, N_numeric, N_exact, decay_constant)

if __name__ == "__main__":
    main()