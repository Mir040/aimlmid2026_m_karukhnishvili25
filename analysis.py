import numpy as np
import matplotlib.pyplot as plt

# Data points extracted from the graph
x = np.array([-10.0, -7.9, -5.1, -3.5, -1.5, 1.9, 3.0, 5.0, 7.0, 8.5])
y = np.array([6.5, 5.9, 3.6, 4.5, 1.7, 0.5, -2.2, -3.0, -4.0, -5.5])

# Pearson correlation coefficient
r = np.corrcoef(x, y)[0, 1]
print("Pearson correlation coefficient:", r)

# Scatter plot with regression line
plt.scatter(x, y)
plt.plot(x, np.poly1d(np.polyfit(x, y, 1))(x))
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Scatter Plot with Regression Line (r = {r:.3f})")
plt.show()
