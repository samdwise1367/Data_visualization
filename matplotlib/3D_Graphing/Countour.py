from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

def temp(x,y):
    value = np.sin(np.sqrt(x**2 + y**2))
    return value

x = np.linspace(-6,6,30)
y = np.linspace(-6,6,30)
x_value,y_value = np.meshgrid(x,y)
z_value = temp(x_value,y_value)
figure = plt.figure()
axis = plt.axes(projection='3d')
axis.contour3D(x_value,y_value,z_value, 50, cmap='binary')
axis.set_xlabel('x')
axis.set_ylabel('y')
axis.set_zlabel('z')
plt.show()