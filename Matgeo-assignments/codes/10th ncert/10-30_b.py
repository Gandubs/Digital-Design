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

#given points
A = np.array([-1,-1]).reshape(-1,1)
B = np.array([-1,6]).reshape(-1,1)
C = np.array([3,6]).reshape(-1,1)
D = np.array([3,-1]).reshape(-1,1)

#coordinates of midpoints
P = (A+B)/2
Q = (B+C)/2
R = (C+D)/2
S = (D+A)/2

#Line parameters for PR AND QS
m1 = dir_vec(P,R)
m2 = dir_vec(Q,S)
n1 = norm_vec(P,R)
n2 = norm_vec(Q,S)

#Intersection point
O = line_intersect(m2,P,n2,Q)
print("Intersection point is : " ,O)
L=(A+B+C+D)/4
print("midpoint is : " ,L)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)
x_PR = line_gen(P,R)
x_QS = line_gen(Q,S)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')
plt.plot(x_PR[0,:],x_PR[1,:],label='$PR$')
plt.plot(x_QS[0,:],x_QS[1,:],label='$QS$')

#Labeling the coordinates
tri_coords = np.block([[A,B,C,D,P,Q,R,S,O]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','P','Q','R','S','O']
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
plt.savefig('/home/krishna/Documents/Matgeo-assignments/figs/10-30_b.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/median.pdf"))
#else
#plt.show()

