# Radioactive Decay Simulation

This Python project simulates the radioactive decay of a material using both:

a numerical method (Euler method with random noise), and an analytical solution based on the exponential decay law.
The simulation also plots and compares the results on the same graph.

## Features:
- Numerical simulation of radioactive decay with a small random noise added.
- Exact analytical solution for comparison.
- Dynamic input of all key parameters: initial number of atoms, decay constant, simulation time, and time step.
- Input validation: the program only accepts numerical values.
- Automatically saves the result as a plot.png file.

## Installation and Running:
# Clone the repository
git clone https://github.com/DeaDragonfly/radioactive-decay-simulation.git

# Navigate into the project folder
cd radioactive-decay-simulation

# Install required packages
pip install matplotlib numpy

# Run the program
python decay_simulation.py

## Model:
dN/dt = -λN

where:
- N is the number of atoms
- λ (lambda) is the decay constant
- time_end is the total simulation time
- dt is the time step

## Scientific Background:
Radioactive decay follows the exponential law:
𝑁(𝑡)=𝑁0⋅𝑒^(−𝜆𝑡)

where:

- N(t) is the number of atoms at time 𝑡,
- 𝑁0 is the initial number of atoms,
- 𝜆 is the decay constant.

In the numerical simulation, a small random noise is added to make the model more realistic and represent natural measurement uncertainties.

## Plot:
When you run the program, you will see a plot comparing:

- Numerical solution (with noise) — solid line
- nalytical solution (perfect curve) — dashed line

## Technologies:
- NumPy
- Matplotlib
- Random

## Future Improvements:
- Add an option to toggle random noise.
- Add multiple simulations for different decay constants on the same plot.
- Implement more accurate integration methods (e.g., Runge-Kutta).
- Allow saving plots with customizable filenames.

## Author:
Mikheyeva Xeniya
Applied Mathematics Student at THWS

April 2025
