import scipy
import matplotlib.pyplot as plt
import math
import numpy as np

# Time Step
t_step = 60 # s
# Initial Time
t_0 = 0

# Gravitational Constant
g = 6.6726 * 10 ** -11 # Nm2kg-2

# Mass of Earth
m_e = 5.9742 * 10 ** 24 # kg
# Mass of Moon
m_m = 7.35 * 10 ** 22 # kg
# Earth-Moon distance
d = 3.844 * 10 ** 8 # m

# Distance from Centre of Mass (CoM)
# to Earth
r_e = d * m_m / (m_m + m_e)
# to Moon
r_m = d * m_e / (m_m + m_e)

# Period of Orbit
p = np.sqrt((4 * np.pi ** 2 * d ** 3) / (g * (m_e + m_m)))
# Angular Velocity
omega = 2 * np.pi / p

# Times
time = np.arange(t_0, p, t_step)


# Positions
# of Earth
x_e = np.zeros(len(time))
y_e = np.zeros(len(time))
z_e = np.zeros(len(time))
# of Moon
x_m = np.zeros(len(time))
y_m = np.zeros(len(time))
z_m = np.zeros(len(time))


# Calculations
for n, t in enumerate(time):
    x_e[n] = r_e * np.cos(omega * t)
    y_e[n] = r_e * np.sin(omega * t)
    x_m[n] = -r_m * np.cos(omega * t)
    y_m[n] = -r_m * np.sin(omega * t)


# Plotting
plt.plot(x_e, y_e)
plt.plot(x_m, y_m)

plt.gca().set_aspect('equal', adjustable='box')
plt.show()