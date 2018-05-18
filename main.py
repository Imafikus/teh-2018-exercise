import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import math


def calc_curr_vx(vx):
    vx = vx
    return vx

def calc_curr_vy(vy):
    vy -= CONST_G * t_curr**2 / 2
    return vy


#constants
CONST_G = 9.81
CONST_STEP = 0.1

#input values
v_start = float(input()) 
alpha_start = float(input())
num_secs = int(input())

#init start vals
t_curr = 0.0
vx_curr = v_start * math.cos(alpha_start)
vy_curr = v_start * math.sin(alpha_start)

x = 0.0
y = 0.0

x_coords = []
y_coords = []


while(t_curr <= float(num_secs)):
    x_coords.append(x)
    
    y_coords.append(y)

    x += vx_curr * t_curr
    y += vy_curr * t_curr

    vx_curr = calc_curr_vx(vx_curr)
    vy_curr = calc_curr_vy(vy_curr)

    t_curr += CONST_STEP

plt.plot(x_coords, y_coords, 'r')
plt.show()
    
     
    


