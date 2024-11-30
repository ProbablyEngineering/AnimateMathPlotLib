import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))  # Initial plot with a sine wave

# Function to update the data for each frame
def update(frame):
    line.set_ydata(np.sin(x + frame / 10))  # Shift the sine wave
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()

# ani.save('sine_wave_animation.mp4', writer='ffmpeg')      # To save the animation as a file