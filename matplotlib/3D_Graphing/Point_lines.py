from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

axis = plt.axes(projection='3d')

#Data for a three-dimensional line4
z_data = np.linspace(0,15,1000)
x_data = np.sin(z_data)
y_data = np.cos(z_data)
axis.plot3D(x_data,y_data,z_data, 'gray')

z = 15*np.random.randn(100)
x = np.sin(z) + 0.1 * np.random.randn(100)
y = np.cos(z) +0.1 * np.random.randn(100)
axis.scatter3D(x,y,z,c = z, cmap='Greens')
plt.show()