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

v1 = [-1,-1,-1]
v2 = [1,-1,-1]
v3 = [1,1,-1]
v4 = [-1,1,-1]
v5 = [-1,-1,1]
v6 = [1,-1,1]
v7 = [1,1,1]
v8 = [-1,1,1]
cube=[v1,v2,v3,v4,v5,v6,v7,v8]


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