from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure()
axis = figure.add_subplot(111, projection = '3d')

x,y,z = axes3d.get_test_data()
axis.plot_wireframe(x,y,z, rstride=2,cstride=2)

axis.set_xlabel('x axis')
axis.set_xlabel('y axis')
axis.set_xlabel('z axis')
plt.legend()
plt.show()