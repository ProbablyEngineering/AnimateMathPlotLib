import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})  # Use polar coordinates for a spiral
ax.set_aspect('equal')  # To make it visually proportional

# Create the initial data for a spiral
theta = np.linspace(0, 10 * np.pi, 500)  # Angles from 0 to 10 * pi
r = theta / np.pi  # Radius increases proportionally to theta/pi
line, = ax.plot(theta, r, color='blue', lw=2)

# Function to update the data for each frame
def update(frame):
    # Adding a dynamic phase shift to the spiral
    r = (theta + frame / 10) / np.pi
    line.set_data(theta, r)
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
