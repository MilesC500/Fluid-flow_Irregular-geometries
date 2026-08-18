import numpy as np
from matplotlib import pyplot as plt

n_steps = 1000
n_trajectories = 500
n_bins = 20

positions_2D = np.empty([n_trajectories, n_steps])

positions_2D[0,:] = 0
positions_2D[:,0] = 0 

for i in range(n_trajectories):
    for j in range (1,n_steps):
        step = 2*int(2*np.random.uniform()) -1   # this will automatically pick +/-1, 50/50
        
        step = step + 0.2 # now it's picking -0.8 or 1.2 automatically...
        positions_2D[i,j] = positions_2D[i,j-1] + step
        
#struggling to get a histogram of the final positions of each trajectory12:30pm
#trying to print a 1-D array of the final 2D positions from first to 50th trajectory 12:41pm

fig, axs = plt.subplots(1,2, tight_layout=True)

# histogram of all paths' final positions
axs[0].hist(positions_2D[:,n_steps-1], bins=n_bins)
# always label axes once things are finalized. Can get very confusing.
axs[0].set(xlabel='position', ylabel='count', title='final position histogram')

# plot of all paths' trajectories in time... this uses each column of the 
# array as a different "y coordinates" and plots them all.
axs[1].plot(np.arange(n_steps), positions_2D.T, alpha=0.1, c='k') #.T means "transpose" (flip rows and columns)

# TODO: you try labeling axs[1] appropriately...

fig.show()
fig.savefig('results.png', bbox_inches='tight') # saving an image to computer automatically
#success!going to try to make an animation going the distribution for 1000 steps 1:00pm


  

#plt.xlabel('steps')
#plt.ylabel('positions')
#plt.show()
