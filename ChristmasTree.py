import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create the figure
fig, ax = plt.subplots()
fig.set_facecolor("midnightblue")
fig.set_size_inches(8, 6, forward=True)
ax.set_facecolor("midnightblue")
ax.axis("off")  # Turn off axes

# Generate tree (triangular layers)
tree_levels = 5
tree_x = []
tree_y = []
for i in range(tree_levels):
    base_width = 10 - i * 2
    tree_x.extend(np.linspace(-base_width / 2, base_width / 2, 100))
    tree_y.extend(np.full(100, i + 1))  # Make the y-coordinates increase as we go up

# Generate trunk
trunk_x = [-0.5, 0.5, 0.5, -0.5, -0.5]
trunk_y = [0, 0, -1, -1, 0]  # Place the trunk below the tree

# Add lights
n_lights = 30
light_positions = np.random.uniform(-5, 5, (n_lights, 2))  # Random light positions within the tree bounds
light_colors = ["gold", "red", "blue", "white"]  # Possible light colors
current_light_colors = np.random.choice(light_colors, n_lights)  # Random initial colors

# Generate snowflakes
n_snowflakes = 50
snowflakes_x = np.random.uniform(-6, 6, n_snowflakes)
snowflakes_y = np.random.uniform(6, 10, n_snowflakes)

# Tree, trunk, and lights setup
tree, = ax.plot(tree_x, tree_y, color="green", lw=2)
trunk, = ax.plot(trunk_x, trunk_y, color="saddlebrown", lw=2)

# Create scatter plot for lights and snowflakes
lights = ax.scatter(light_positions[:, 0], light_positions[:, 1], color=current_light_colors, s=50)
snowflakes = ax.scatter(snowflakes_x, snowflakes_y, color="white", s=20)

# Update function for animation
def update(frame):
    # Twinkling lights
    global current_light_colors
    current_light_colors = np.random.choice(light_colors, n_lights)  # Change light colors
    lights.set_color(current_light_colors)

    # Falling snow
    global snowflakes_y
    snowflakes_y -= 0.1  # Snowflakes fall down
    snowflakes_y[snowflakes_y < 0] = 10  # Reset snowflakes that fall below the screen
    snowflakes.set_offsets(np.c_[snowflakes_x, snowflakes_y])  # Update snowflake positions

    return tree, trunk, lights, snowflakes

# Animation
ani = FuncAnimation(fig, update, frames=100, interval=100, blit=False, save_count=0)

plt.show()
