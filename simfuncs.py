import numpy as np
import h5py
from tkinter import Tk
from tkinter import filedialog
from matplotlib import pyplot as plt

def coord_sim(points, stepsize):

    # simulates 3D diffusion coordinate data, in spherical coordinates
    # stepsize must be given in degrees

    phi = np.zeros(points)
    theta = np.zeros(points)

    rng = np.random.default_rng()

    step_options = [-stepsize, stepsize]
    binary_options = [0,1]

    steps = rng.choice(step_options, points)

    binary_choice_phi = rng.choice(binary_options, points)
    binary_choice_theta = 1-binary_choice_phi

    steps_phi = steps * binary_choice_phi
    steps_theta = steps * binary_choice_theta

    phi = phi + steps_phi
    theta = theta + steps_theta

    phi_traj = np.cumsum(phi)
    theta_traj = np.cumsum(theta)

    return [phi_traj, theta_traj]

def cart_coords(angles, radius, time_axis):

    phi_angles = angles[0]
    theta_angles = angles[1]
    r=[]

    if time_axis == True:
        r = np.linspace(0.01, 1, len(phi_angles))
    elif time_axis == False:
        r = np.full(phi_angles.shape, radius)

    x = r*np.cos(theta_angles)*np.cos(phi_angles)
    y = r*np.cos(theta_angles)*np.sin(phi_angles)
    z = r*np.sin(theta_angles)

    return [x, y, z]

def scatter3D(coords, plot_time, show):

    coords = cart_coords(coords, radius=1, time_axis=plot_time)

    ax = plt.figure().add_subplot(projection='3d')

    around_circle = np.linspace(0, 2*np.pi,1000)
    ax.plot(np.sin(around_circle), np.cos(around_circle), np.full(around_circle.shape, 0), color="black", linewidth=1)
    ax.plot(np.sin(around_circle), np.full(around_circle.shape, 0), np.cos(around_circle), color="black", linewidth=1)
    ax.plot(np.full(around_circle.shape, 0), np.sin(around_circle), np.cos(around_circle), color="black", linewidth=1)
    
    ax.scatter(coords[0], coords[1], coords[2], s=1)

    if show == True:
        plt.show()
    else: 
        plt.clf()
        plt.close()  
    
def save_data(filepath, coords, params):

    root = Tk()
    root.withdraw()

    path = filedialog.askdirectory()

    hf_name = path + "/Simdata_" + str(params[0]) + "sims_" + str(params[1]) + "steps_" + str(params[2]) + "size" ".h5"

    hf = h5py.File(hf_name, "w")

    hf.create_dataset("Parameters", data=params)
    hf.create_dataset("Phi_Coords", data=coords[0])
    hf.create_dataset("Theta_Coords", data=coords[1])

    hf.close()
