import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import math


def calc_curr_vx(vx):
    vx -= vx**2 * CONST_DELTA_T * CONST_K
    return vx

def calc_curr_vy(vy):
    sgn_y = abs(vy) / vy
    vy -= vy**2 * CONST_DELTA_T * CONST_K * sgn_y
    vy -= CONST_G * t_curr
    return vy

#constants
CONST_G = 9.81
CONST_DELTA_T = 0.1
CONST_K = 0.01

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

#main loop
while(t_curr <= float(num_secs)):
    x_coords.append(x)
    y_coords.append(y)

    x += vx_curr * CONST_DELTA_T
    y += vy_curr * CONST_DELTA_T
  
    vx_curr = calc_curr_vx(vx_curr)
    vy_curr = calc_curr_vy(vy_curr)

    t_curr += CONST_DELTA_T

#plot graph
plt.plot(x_coords, y_coords, 'r')
plt.show()
    
     
    


