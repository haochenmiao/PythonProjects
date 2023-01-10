import numpy as np
import matplotlib.pyplot as plt
import scipy.io

# load yalefaces
yalefaces = scipy.io.loadmat("yalefaces.mat")
X = yalefaces["X"]

# display the first nine images
fig, ax = plt.subplots(3, 3, figsize=(8, 8))
for i in range(9):
    ax[i // 3, i % 3].imshow(X[:, i].reshape(32, 32), cmap="gray")
    ax[i // 3, i % 3].axis("off")
plt.show()

m = 100
Xm = X[:,:m]
C = Xm.T @ Xm
A1 = C

score_max = 0
r_max, c_max = None, None
for j in range(m-1):
    for k in range(j+1, m):
        if C[j, k] > score_max:
            score_max = C[j, k]
            r_max, c_max = j, k

print("r_max:", r_max)
print("c_max:", c_max)
print("score_max:", score_max)
A2 = [r_max, c_max]

score_min = np.inf
r_min, c_min = None, None
for j in range(m-1):
    for k in range(j+1, m):
        if C[j, k] < score_min:
            score_min = C[j, k]
            r_min, c_min = j, k

print("r_min:", r_min)
print("c_min:", c_min)
print("score_min:", score_min)
A3 = [r_min, c_min]

# Xs = X[:,image]
image = [1, 313, 512, 5, 2400, 113, 1024, 87, 314, 2005]
Xs = X[:, image]

# Cm = Xs.'*Xs
Cm = np.dot(Xs.T, Xs)
A4 = Cm

# Y = X * (X.')
Y = np.dot(X, X.T)

# [V,D] = eigs(Y,6,'lm')
eigen_values, eigen_vectors = np.linalg.eig(Y)
idx = eigen_values.argsort()[-6:][::-1]
V = eigen_vectors[:, idx]

# A5 = abs(V)
A5 = np.abs(V)

u, s, v = np.linalg.svd(X)
A6 = u[:,:6]

v1 = V[:,0]
u1 = u[:,0]
A7 = np.linalg.norm(v1-u1)

singval = np.diag(s)
lar6sing = singval[:6]
Sum = np.sum(singval)
A8 = 100 * np.abs([lar6sing[i]/Sum for i in range(6)])
