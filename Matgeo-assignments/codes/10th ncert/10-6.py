#Code by GVV Sharma
#September 23, 2023
#released under GNU GPL
#Altitudes of a triangle
#Orthocentre


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/krishna/Documents/Matgeo-assignments/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
#import subprocess
#import shlex
#end if


#Given points
A = np.array([2,0]).reshape(-1,1)
B = np.array([6,0]).reshape(-1,1) 

#Find other end point
C = 2*A-B
print("The other endpoint is : " ,C)

#radius vec
m1 = dir_vec(A,B)

#Radius length
r =LA.norm(B-A)
print("The radius is : " ,r)

#Generating AB and AC
x_AB = line_gen(A,B)
x_AC = line_gen(A,C)


#generating circle
x_circ= circ_gen(A,r)

#Plotting AB
plt.plot(x_AB[0,:],x_AB[1,:],'--',label='$AB$')
plt.plot(x_AC[0,:],x_AC[1,:],'--',label='$AC$')


#plotting
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')


#Labeling the coordinates
tri_coords = np.block([[A,B,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
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
plt.savefig('/home/krishna/Documents/Matgeo-assignments/figs/10-6.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/altitude.pdf"))
#else
#plt.show()
