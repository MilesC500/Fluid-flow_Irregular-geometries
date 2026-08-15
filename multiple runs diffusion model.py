import numpy as np
import matplotlib as plt

n_steps = 1000
n_trajectories = 50

positions_2D = np.empty([n_trajectories, n_steps])

positions_2D[0,:] = 0
positions_2D[:,0] = 0 

for i in range(1,n_trajectories):
    for j in range (1,n_steps):
        rabd = np.random.uniform()
        if rabd >0.5:
            positions_2D[i,j] = positions_2D[i, j-1] + 1
        else:
            positions_2D[i,j] = positions_2D[i, j-1] - 1
    for i in range(1,n_trajectories):
        plt.plot(positions_2D[i,:])
        
#struggling to get a histogram of the final positions of each trajectory12:30pm
#trying to print a 1-D array of the final 2D positions from first to 50th trajectory 12:41pm
path_ending_pos_iterable = (positions_2D[i,n_steps-1] for i in range(1,n_trajectories))
dist1 = np.fromiter(path_ending_pos_iterable,int) 
#print(dist1)

#success!going to try to make a histogram using dist1 12:51pm

fig, axs = plt.subplots(1,2, sharey=True, tight_layout=True)
axs[0].hist(dist1, bins=n_bins)
    

      
 
#success!going to try to make an animation going the distribution for 1000 steps 1:00pm


  

plt.xlabel('steps')
plt.ylabel('positions')
plt.show()
