import numpy as np
import simfuncs as sf

#--------------------------------------------------------------
# Simple script to simulate 3D-random diffusion along a sphere
#--------------------------------------------------------------

number_of_steps = 10000
sim_stepsize = 30

param_list = [number_of_steps, sim_stepsize]

angles = sf.coord_sim(points=number_of_steps, stepsize=1)

angles_rad = [np.radians(angles[0]), np.radians(angles[1])]

sf.scatter3D(angles_rad, plot_time=False, show=True)

sf.save_data(coords=angles_rad, params=param_list)