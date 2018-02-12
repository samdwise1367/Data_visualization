from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

figure = plt.figure()
axis = figure.add_subplot(111, projection = '3d')

x= [1,3,4,5,6,6,7,8,9,10]
y = [6,3,4,3,4,5,6,4,5,6]
z = [7,5,6,4,5,6,7,8,5,6]

x2= [-1,-3,-4,-5,-6,-6,-7,-8,-9,-10]
y2 = [-6,-3,-4,-3,-4,-5,-6,-4,-5,-6]
z2 = [7,5,6,4,5,6,7,8,5,6]

axis.scatter(x,y,z, c='r',marker='o', label='red')
axis.scatter(x2,y2,z2, c='g',marker='o', label='green')

axis.set_xlabel('x axis')
axis.set_xlabel('y axis')
axis.set_xlabel('z axis')
plt.legend()
plt.show()