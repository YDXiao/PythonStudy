import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Create a list of evenly-spaced numbers over the range
x = np.linspace(0, 20, 500)
plt.title('Test')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot
