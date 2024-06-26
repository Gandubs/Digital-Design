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

#given point
A = np.array([3,-5]).reshape(-1,1)

#coordinate of other point is (x,-5) so

coefficients = [1, -6, -216]
roots = np.roots(coefficients)
print(roots)

B = np.array([roots[0],-5])
C = np.array([roots[1],-5])


#Generating all lines
x_AB = line_gen(A,B)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

#Labeling the coordinates
tri_coords = np.block([[A,B,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C',]
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
plt.savefig('/home/krishna/Documents/Matgeo-assignments/figs/10-14.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/median.pdf"))
#else
#plt.show()

