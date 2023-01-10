import numpy as np
import scipy.linalg as la

A1 = np.zeros((51, 3))
v_1 = np.arange(0, 101, 2)
A = np.array([[70, -20, -10], [-20, 55, -10], [-10, -10, 50]])

for j in range(51):
    v1 = v_1[j]
    b = np.array([v1, 0, 200])
    x = np.linalg.solve(A, b)
    A1[j, :] = x

A2 = np.zeros((51, 3))

for j in range(51):
    v1 = v_1[j]
    b = np.array([v1, 0, 200])
    P, L, U = la.lu(A)
    y = np.linalg.solve(L, np.dot(P, b))
    x = np.linalg.solve(U, y)
    A2[j, :] = x

tol = 1e-6
A3 = np.zeros((51, 3))

for j in range(51):
    v1 = v_1[j]
    I1, I2, I3 = 0, 0, 0
    for k in range(100):
        I1 = (v1 + 20*I2 + 10*I3)/70
        I2 = (0 + 20*I1 + 10*I3)/55
        I3 = (200 + 10*I1 + 10*I2)/50
        B = [I1, I2, I3]
        b = [I1, I2, I3]
        Norm = np.linalg.norm(np.abs(np.array(B) - np.array(b)))

        if Norm < tol:
            break
    A3[j, :] = [I1, I2, I3]

A4 = np.zeros((51, 3))

for j in range(51):
    v1 = v_1[j]
    I1, I2, I3 = 0, 0, 0
    for k in range(100):
        I1 = (v1 + 20*I2 + 10*I3)/70
        I2 = (0 + 20*I1 + 10*I3)/55
        I3 = (200 + 10*I1 + 10*I2)/50
        B = [I1, I2, I3]
        b = [I1, I2, I3]
        Norm = np.linalg.norm(np.abs(np.array(B) - np.array(b)))

        if Norm < tol:
            break
    A4[j, :] = [I1, I2, I3]

A5 = np.zeros((1, 2))
A5[0, 0] = np.sum(A3[:, 2])/51
A5[0, 1] = np.sum(A4[:, 2])/51