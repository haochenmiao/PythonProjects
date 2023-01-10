import numpy as np
from scipy.integrate import solve_ivp

# solve epsilom = 0.1 using Van der pol differential equation
def vanderpoldemo(t, y, epsilon):
    dy = np.zeros(2)
    dy[0] = y[1]
    dy[1] = epsilon*(1 - y[0]**2)*y[1] - y[0]
    return dy

tspan = np.arange(0, 30.5, 0.5)
epsilon = 0.1
y0 = [0.1, -1]

sol = solve_ivp(lambda t, y: vanderpoldemo(t, y, epsilon), [tspan[0], tspan[-1]], y0, t_eval=tspan)
A1 = sol.y

# Solve epsilon = 1 using van der pol differential equation
epsilon = 1
sol = solve_ivp(lambda t, y: vanderpoldemo(t, y, epsilon), [tspan[0], tspan[-1]], y0, t_eval=tspan)
A2 = sol.y

# Solve epsilon = 20 using van der pol differential equation
epsilon = 20
sol = solve_ivp(lambda t, y: vanderpoldemo(t, y, epsilon), [tspan[0], tspan[-1]], y0, t_eval=tspan)
A3 = sol.y

# Solve piecewise problem using van der pol differential equation
tspan1 = np.arange(0, 10.5, 0.5)
y01 = [0.1, -1]
sol1 = solve_ivp(lambda t, y: vanderpoldemo(t, y, 0.1), [tspan1[0], tspan1[-1]], y01, t_eval=tspan1)
y1 = sol1.y

tspan2 = np.arange(10, 20.5, 0.5)
y02 = [y1[-1, 0], y1[-1, 1]]
sol2 = solve_ivp(lambda t, y: vanderpoldemo(t, y, 1), [tspan2[0], tspan2[-1]], y02, t_eval=tspan2)
y2 = sol2.y
y03 = [y2[-1, 0], y2[-1, 1]]

tspan3 = np.arange(20, 30.5, 0.5)
sol3 = solve_ivp(lambda t, y: vanderpoldemo(t, y, 20), [tspan3[0], tspan3[-1]], y03, t_eval=tspan3)
y3 = sol3.y

A4 = np.concatenate((y1, y2[:, 1:], y3[:, 1:]), axis=1)
