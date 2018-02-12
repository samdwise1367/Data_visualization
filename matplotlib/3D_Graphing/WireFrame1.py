#Code to visualize wireframe
#By Samson Oni
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

figure = plt.figure()
axis = figure.add_subplot(111, projection = '3d')

x= [1,3,4,5,6,6,7,8,9,10]
y = [6,3,4,3,4,5,6,4,5,6]
z = [7,5,6,4,5,6,7,8,5,6]

axis.plot_wireframe(x,y,z)

axis.set_xlabel('x axis')
axis.set_xlabel('y axis')
axis.set_xlabel('z axis')
plt.legend()
plt.show()