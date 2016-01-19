import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(-30., 30., 0.01)
x_ticks = range(-20, 21)
y_ticks = range(-10, 11)

plt.plot([-1000, 1000],[0, 0])
plt.plot([0, 0],[-1000, 1000])

# plot axes
plt.plot(t, 0 * t)
plt.plot(0 * t, t)

#gradients
a, b, c, d, e, f = [1, 2, 3, -1, -2, -3]

# plot the graphs
graphs = plt.plot(t, a*t, 'r', t, b*t, 'b', t, c*t, 'g', t, d*t, 'y', t, e*t, 'c', t, f*t, 'm')
plt.legend(graphs, ["y = %d.x"%a, "y = %d.x"%b, "y = %d.x"%c, "y = %d.x"%d, "y = %d.x"%e, "y = %d.x"%f])

# label the axes
plt.xlabel("x axis", horizontalalignment='left')
plt.ylabel("y axis")
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.axis([-20, 20, -10, 10]);

# draw a grid
plt.grid(True)

plt.show()
