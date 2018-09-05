# Compare solution ode euler method and odeint
# ODE problems are important in computational physics, so we will look at one more example: the damped harmonic
# oscillation. This problem is well described on the wiki page: http://en.wikipedia.org/wiki/Damping
# The equation of motion for the damped oscillator is:
# xdd+2*zeta*omega_0*xd+omega_0^2*x=0
# where  x  is the position of the oscillator,  ω0  is the frequency, and  ζ  is the damping ratio.
# To write this second-order ODE on standard form we introduce  p=dxdt :
# dx_1=x_2
# dx_2=−2*zeta*omega_0*x_2−omega_0^2*x_1
#
# In the implementation of this example we will add extra arguments to the RHS function for the ODE,
# rather than using global variables as we did in the previous example.
# As a consequence of the extra arguments to the RHS, we need to pass an keyword argument args to the odeint function:

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# discrete time solution
def Dy(y, dt, tend, zeta, w0):
    A = np.array([[0, 1], [-w0**2, -2*zeta*w0]])
    sol = np.array(y)
    sol = np.expand_dims(sol, axis=0)

    tt = np.arange(0, tend, dt)
    for t in tt[1:]:
        sol = np.vstack((sol, sol[-1, :] + dt*np.dot(sol[-1, :], A.T)))

    return tt, sol

# continuous time solution
def dy(y, t, zeta, w0):
    """
    The right-hand side of the damped oscillator ODE
    """
    x, p = y[0], y[1]

    dx = p
    dp = -2 * zeta * w0 * p - w0 ** 2 * x

    return [dx, dp]


# initial state:
y0 = [1.0, 0.0]

# time coordinate to solve the ODE for
t = np.linspace(0, 10, 1000)
w0 = 2*np.pi*1.0
dt = 0.001
tend = 10

# solve the ODE problem for three different values of the damping ratio
y1  = odeint(dy, y0, t, args=(0.0, w0))  # undamped
tt, y1d = Dy(y0, dt, tend, 0.0, w0)
y2 = odeint(dy, y0, t, args=(0.2, w0))  # under damped
y3 = odeint(dy, y0, t, args=(1.0, w0))  # critial damping
y4 = odeint(dy, y0, t, args=(5.0, w0))  # over damped

fig, ax = plt.subplots(4, 1)
ax[0].plot(t, y1[:, 0], 'k', label="undamped")
ax[0].plot(tt, y1d[:, 0], 'k--', label="undamped discrete time")
ax[1].plot(t, y2[:, 0], 'r', label="under damped")
ax[2].plot(t, y3[:, 0], 'b', label=r"critical damping")
ax[3].plot(t, y4[:, 0], 'g', label="over damped")
for axis in ax:
    axis.legend()

plt.show()

