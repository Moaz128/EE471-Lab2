# Moaz Alhamdan
# ID: 1741735
# Program to plot matlab file given in the lab section of the EE471 course
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np


# Function for plotting a square wave, it takes in a parameter for x, y, and a matplotlib axes to draw on
# The code inside the function is mostly for plot aesthetic
def plotsquarewave(ch_x, ch_y, ax):
    ax.plot(ch_x, ch_y)
    ax.set_xlim(ch_x[0], ch_x[len(ch_y) - 1])
    yticks = np.arange(-12, 16, 2)
    ax.minorticks_on()
    ax.set_yticks(yticks)
    ax.grid(True)
    ax.set_xlabel('Time in ms')
    ax.set_ylabel('Amplitude in volts')
    ax.set_title('Square wave')


# Function for plotting a triangle wave, it takes in a parameter for x, y, and a matplotlib axes to draw on
# The code inside the function is mostly for plot aesthetic
def plottrianglewave(ch_x, ch_y, ax):
    ax.plot(ch_x, ch_y)
    ax.set_xlim(ch_x[0], ch_x[len(ch_x) - 1])
    ax.minorticks_on()
    ax.grid(True)
    ax.set_xlabel('Time in ms')
    ax.set_ylabel('Amplitude in volts')
    ax.set_title('Triangle wave')


# Here we load the matlab file
lowMV = loadmat('EE471_LabII_Exp_2_100n_capacitor')

# Extract the axis values from the dictionary variable
CH1_x = lowMV.get('time_axis')
CH1_y = lowMV.get('time_trace')
CH2_x = lowMV.get('time_axis_ch2')
CH2_y = lowMV.get('time_trace_ch2')

# Convert type of values from standing vector to 1D array and convert s to ms for easier readings
CH1_x = CH1_x[0] * 1000
CH1_y = CH1_y[0]
CH2_x = CH2_x[0] * 1000
CH2_y = CH2_y[0]

# initiate matplotlib objects for plotting
fig, (ax1, ax2) = plt.subplots(1, 2)

# call plotting functions
plotsquarewave(CH1_x, CH1_y, ax1)
plottrianglewave(CH2_x, CH2_y, ax2)

# Show the plot
plt.show()




