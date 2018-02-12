#Code to show an example of 3D visualisation of bar char
#By Samson Oni
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure()
axis = figure.add_subplot(111, projection = '3d')

x= [1,3,4,5,6,6,7,8,9,10]
y = [6,3,4,3,4,5,6,4,5,6]
z = np.zeros(10)

x_d = np.ones(10)
y_d = np.ones(10)
z_d = [1,2,3,4,5,6,7,8,9,10]

axis.bar3d(x,y,z,x_d,y_d,z_d)

axis.set_xlabel('x axis')
axis.set_xlabel('y axis')
axis.set_xlabel('z axis')
plt.legend()
plt.show()