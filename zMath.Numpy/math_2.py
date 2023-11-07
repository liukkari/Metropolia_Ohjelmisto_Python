from matplotlib import pyplot as plt, patches
import numpy as np

fig = plt.figure(figsize=(6.4, 4.8))
ax = fig.subplots()

# Increase the radius of the circle to make it larger
ymp = patches.Circle((0, 0), radius=2, fill=0, color='lightgray', linestyle='dashed')
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to center, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

# Set custom x-axis labels with π and fractions
x_ticks = [-3 * np.pi, -2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi, 3 * np.pi]
x_labels = ['$-3\pi$', '$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$', '$3\pi$']
plt.xticks(x_ticks, labels=x_labels, minor=False)
plt.yticks([-2, -1, 0, 1, 2], minor=False)

x_values = np.linspace(-3 * np.pi, 3 * np.pi, 400)
y_values = np.sin(x_values)

# Adjust line colors and styles
ax.plot(x_values, y_values, color='blue', linestyle='--', label='sin(x)')

# Add markers for specified angles on the unit circle and label them
angles = [30, 45, 60, 90, 120, 150, 180, 270]
for angle in angles:
    radian_angle = np.radians(angle)
    x = np.cos(radian_angle) * 2  # Adjust for the larger circle radius
    y = np.sin(radian_angle) * 2  # Adjust for the larger circle radius
    ax.plot(x, y, 'ro')  # 'ro' represents a red circle marker
    ax.text(x, y, str(angle), ha='right', va='bottom')

# Add a legend for the markers
ax.legend(['sin(x)', 'Points'], loc='upper right', fontsize=12)

plt.show()

