import numpy as np
import matplotlib as plt

n_steps = 1000
n_trajectories = 50

positions_2D = np.empty(n_trajectories, n_steps)

positions_2D[0,:] = 0
positions_2D[:,0] = 0 

for i in range(1,n_trajectories):
    for j in range (1,n_steps):
        rabd = np.random.uniform()
        if rabd >0.5:
            positions_2D[:j] = positions_2D[i, j-1] + 1
        else:
            positions_2D[:j] = positions_2D[i, j-1] - 1

plt.plot(positions_2D)
plt.xlabel('steps')
plt.ylabel('positions_2D')
plt.show()
