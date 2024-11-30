import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
x_data = []
y_data = []
line, = ax.plot([], [], lw=2)

# Initialize the axes limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

# Function to update the data for each frame
def update(frame):
    x_data.append(frame / 10) 
    y_data.append(np.sin(frame / 10)) 
    line.set_data(x_data, y_data) 

    # Dynamically adjust x-axis limits
    if x_data[-1] > ax.get_xlim()[1]:
        ax.set_xlim(0, x_data[-1] + np.pi) 

    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(200), interval=45, blit=False)

plt.show()

# ani.save('sine_wave_animation.mp4', writer='ffmpeg')      # To save the animation as a file
