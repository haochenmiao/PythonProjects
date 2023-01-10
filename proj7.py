import numpy as np
from scipy.interpolate import interp1d, UnivariateSpline
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# f(x) = Ax^2 + Bx + C
# Fit the data with parabolic fit and calculate E2 error
x = np.array(range(1, 25))
y = [75, 77, 76, 73, 69, 68, 63, 59, 57, 55, 54, 52, 50, 50, 49, 49, 49, 50, 54, 56, 59, 63, 67, 72]

pcoeff = np.polyfit(x, y, 1)
xp = np.linspace(1, 24, 1000)
yp = np.polyval(pcoeff, xp)
pcoeff2 = np.polyfit(x, y, 2)

yp3 = np.polyval(pcoeff2, x)
n = len(x)
E2 = np.sqrt(np.sum((np.abs(yp3 - y))**2)/n)
A1 = E2

# the parabolic fit by using polyfit and polyval
ypn = np.polyval(pcoeff2, xp)
A2 = ypn

# use interpi and spline for the interpolated approximation
yint = interp1d(x, y, kind='cubic')(xp)
A3 = yint

yspline = UnivariateSpline(x, y)
A4 = yspline(xp)

# The error for the least-squares algorithm
def gauss_fit(x0,x,y):
    A = x0[0]
    B = x0[1]
    C = x0[2]
    E = sum((A*np.cos(B*x)+C-y)**2)
    return E

coeff = minimize(gauss_fit, [15, 0.2, 65], args = (x, y))
a1 = coeff.x[0]
B1 = coeff.x[1]
C1 = coeff.x[2]

A5 = np.sqrt(np.sum((np.abs(a1*np.cos(B1*x)+C1-y))**2)/n)

# evaluating the curve for x = 1:0.01:24
A6 = a1*np.cos(B1*xp) + C1
plt.figure(1)
plt.plot(x, y, 'o', xp, A6, 'm', linewidth=2)

# Fitting the least-squares curve
def gauss_fit1(x0,x1,v):
    A = x0[0]
    B = x0[1]
    C = x0[2]
    D = x0[3]
    return sum((A*np.cos(B*x1)+C*x1+D-v)**2)


x1 = np.array(range(0, 31))
v = [30, 35, 33, 32, 34, 37, 39, 38, 36, 36, 37, 39, 42, 45, 45, 41, 40, 39, 42, 44, 47, 49, 50, 49, 46, 48, 50, 53, 55,
     54, 53]
coeff1 = minimize(gauss_fit1, [3, np.pi / 4, 2 / 3, 32], args=(x1, v))

D = coeff1.x[0]
E = coeff1.x[1]
F = coeff1.x[2]
G = coeff1.x[3]
xp1 = np.linspace(0, 30, 1000)
A7 = D*np.cos(E*xp1) + F*xp1 + G
