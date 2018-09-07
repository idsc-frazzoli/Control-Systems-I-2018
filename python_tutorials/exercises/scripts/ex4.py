# Compare solution ode euler method and odeint

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Discretized solution
def dyDt(y, dt, tend, zeta, w0):
    A = np.array([[0, 1], [-w0**2, -2*zeta*w0]])
    M = A*dt + np.eye(2)
    sol = np.array(y)

    # need to expand dimension to be consistent (alternatively use np.matrix())
    sol = np.expand_dims(sol, axis=0)

    tt = np.arange(0, tend, dt)
    for t in tt[1:]:
        sol = np.vstack((sol, np.dot(sol[-1, :], M.T)))

    return sol


# Continuous time solution
def dyCt(y, t, zeta, w0):
    """
    The right-hand side of the damped oscillator ODE
    """
    x_1, x_2 = y[0], y[1]

    dx_1 = x_2
    dx_2 = -2 * zeta * w0 * x_2 - w0 ** 2 * x_1

    return [dx_1, dx_2]


# initial state:
y0 = [1.0, 0.0]

# params dictionary
params = {"zeta": [0.0, 0.2, 1.0, 5.0], "w0": 2*np.pi*1.0,
          "label": ["Undamped", "Damped", "Critical", "Overdamped"]}

# time coordinate to solve the ODE with odeint
t_c = np.linspace(0, 10, 1000)

# time coordinate to solve the ODE with Euler approximation
dt = 0.01
tend = 10
t_d = np.arange(0, tend, step=dt)

# use latex font annd generate axis
matplotlib.rcParams.update({'font.size': 14, 'text.usetex': True})
fig, ax = plt.subplots(4, 1, figsize=(10, 18), sharex=True)

for i in range(4):
    y_c = odeint(dyCt, y0, t_c, args=(params["zeta"][i], params["w0"]))
    y_d = dyDt(y0, dt, tend, params["zeta"][i], params["w0"])

    ax[i].plot(t_c, y_c[:, 0], label=r"continuous time")
    ax[i].plot(t_d, y_d[:, 0], "--", label=r"discrete time")

    ax[i].set_title(params["label"][i])
    ax[i].set_ylabel("x")
    ax[i].legend()
    ax[i].grid()

ax[3].set_xlabel("time")
plt.show()

