from lines import *
import math
from random import randint
l = Lines(640, 480)

x_mid = 250
y_mid = 250

#l.addLine((x_mid, y_mid), (x_mid, y_mid+25))
#l.addLine((x_mid+12.5, y_mid+12.5), (x_mid, y_mid+25))
#l.addLine((x_mid+12.5, y_mid+12.5), (x_mid+12.5, y_mid-12.5))
#l.addLine((x_mid-12.5, y_mid+12.5), (x_mid, y_mid+25))
#l.addLine((x_mid-12.5, y_mid-12.5), (x_mid-12.5, y_mid+12.5))

#l.addLine((225, 225), (250, 250))
#l.addLine((250, 250), (275, 225))
#l.addLine((250, 200), (275, 225))
#l.addLine((250, 200), (225, 225))
base=250
basex=275
basey=225
v0 = [-50,-50,-50]         #
v1 = [50,-50,-50]          #
v2 = [50,50,-50]           #
v3 = [-50,50,-50]          #
v4 = [-50,-50,50]          #
v5 = [50,-50,50]           #
v6 = [50,50,50]            #
v7 = [-50,50,50]           #
cube=[v0,v1,v2,v3,v4,v5,v6,v7]

#front
l.addLine(((base+cube[0][0]),(base+cube[0][1])),((base+cube[1][0]),(base+cube[1][1])))
l.addLine(((base+cube[1][0]),(base+cube[1][1])),((base+cube[2][0]),(base+cube[2][1])))
l.addLine(((base+cube[2][0]),(base+cube[2][1])),((base+cube[3][0]),(base+cube[3][1])))
l.addLine(((base+cube[3][0]),(base+cube[3][1])),((base+cube[4][0]),(base+cube[4][1])))

#back
l.addLine(((basex+cube[4][0]),(basey+cube[4][1])),((basex+cube[5][0]),(basey+cube[5][1])))
l.addLine(((basex+cube[5][0]),(basey+cube[5][1])),((basex+cube[6][0]),(basey+cube[6][1])))
l.addLine(((basex+cube[6][0]),(basey+cube[6][1])),((basex+cube[7][0]),(basey+cube[7][1])))
l.addLine(((basex+cube[7][0]),(basey+cube[7][1])),((basex+cube[8][0]),(basey+cube[8][1])))

def vec_tra(vx1, vy1, vx2, vy2):
    return ((vx1+vx2), (vy1+vy2))

def vec_sch(vx, vy, sx , sy):
    return ((vx*sx),(vy*sy))

def vec_rot(vx, vy, h):
    return ((vx*math.cos(h))-(vy*math.sin(h)), (vx*math.sin(h))+(vy*math.cos(h)))

def mat_rot_y(vx, vy, vz, h):
    return(vx*math.cos(h)+vz*math.sin(h), vy, -vx* math.sin(h) + vz* math.cos(h))

def mat_rot_x(vx, vy, vz, h):
    return(vx, vy*math.cos(h)-vz*math.sin(h),vy*math.sin(h)+vz*math.cos(h))

def mat_rot_z(vx, vy, vz, h):
    return(vx*math.cos(h)-vy*math.sin(h),vx*math.sin(h)+vy*math.cos(h),vz)














l.draw()