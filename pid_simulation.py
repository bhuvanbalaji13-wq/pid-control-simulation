import numpy as np
import matplotlib.pyplot as plt

# Time
t = np.linspace(0, 10, 100)

# Desired value
setpoint = 1

# System output
output = np.zeros(len(t))

# PID constants
Kp = 2.0
Ki = 0.5
Kd = 1.0

error_sum = 0
prev_error = 0

for i in range(1, len(t)):
    error = setpoint - output[i-1]
    error_sum += error
    d_error = error - prev_error

    control = Kp*error + Ki*error_sum + Kd*d_error
    output[i] = output[i-1] + control*0.1

    prev_error = error

# Plot
plt.plot(t, output, label="PID Output")
plt.axhline(setpoint, linestyle='--', label="Setpoint")
plt.xlabel("Time")
plt.ylabel("Output")
plt.title("PID Control System Response")
plt.legend()
plt.show()
