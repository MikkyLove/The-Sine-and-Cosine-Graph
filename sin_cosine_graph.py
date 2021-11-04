



import matplotlib.pyplot as plt, numpy as np

n = 1000
xmax, xmin = 2*np.pi, -2*np.pi
x = np.linspace(xmax, xmin, n)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, "r:", label="Sin graph")
plt.plot( x, y2, "m--", label="Cosine graph")

plt.title("A Sin and Cosine Graph!")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()


