import matplotlib.pyplot as plt
import numpy as np

POINT_SIZE = 9

# Import theta and r values from csv file, while skipping the first two rows (headers).
theta = np.genfromtxt('data/galaxymeasures.csv', delimiter=',', skip_header=2, usecols=(2, 3, 4))

# Get r from 14th column (radial velocity)
r = np.genfromtxt('data/galaxymeasures.csv', delimiter=',', skip_header=2, usecols=(14,))

# Convert theta to hours
theta = theta[:,0] + theta[:,1]/60 + theta[:,2]/3600
# Convert theta to radians for plotting
theta = theta * np.pi/12

# Testing
print(theta)
print(r)

# Create a polar plot
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
# Plot the data
ax.scatter(theta, r, s=POINT_SIZE, alpha=0.69)  # Set slightly transparent

# Change theta tick marks to hours with a range from 12h to 16h
ax.set_xticks(np.linspace(12, 16, 5)*np.pi/12)
ax.set_xticklabels(['12h', '13h', '14h', '15h', '16h'])


# Set thetamin to 12h and thetamax to 16h
ax.set_thetamin(12*360/24)
ax.set_thetamax(16*360/24)

# Add axis labels (technically the wrong way around, but label locations actually match properly this way)
ax.set_ylabel('Right Ascension (hours)')
ax.set_xlabel('Radial Velocity (km/s)')
# Move the x-axis label to the top
ax.xaxis.set_label_position('top')
# Move y-axis label to the left a bit
ax.yaxis.labelpad = 10

# Add a title
ax.set_title("Galaxy Radial Velocity (km/s) vs. Right Ascension (hours)")

plt.show()