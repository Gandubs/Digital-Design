import sys                                          #for path to external scripts
sys.path.insert(0, '/home/krishna/Documents/Matgeo-assignments/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
#import subprocess
#import shlex
#end if

#given lines 2x+5y=-4 and 4x-3y=5
A = np.array([[2, 5],
              [4, -3]])
B = np.array([-4, 5])
C_0 = np.linalg.solve(A, B)
print("The point of intersection is : " ,C_0)

#labelling 2 random points of lines and getting POI
C = np.array([C_0[0],C_0[1]]).reshape(-1,1)
D = np.array([-2,0]).reshape(-1,1)
E = np.array([5,5]).reshape(-1,1)

#Generating all lines
x_DC = line_gen(D,C)
x_EC = line_gen(E,C)

#Plotting all lines
plt.plot(x_DC[0,:],x_DC[1,:],label='$DC$')
plt.plot(x_EC[0,:],x_EC[1,:],label='$EC$')

#Labeling the coordinates
tri_coords = np.block([[D,E,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['D','E','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/home/krishna/Documents/Matgeo-assignments/figs/10-24.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/median.pdf"))
#else
#plt.show()

