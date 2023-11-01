import numpy as np
import math

phi = 45*np.pi/180
theta = 45*np.pi/180

rot_mat = np.array([[np.cos(phi)*np.cos(theta), -np.cos(phi)*np.sin(theta), np.sin(phi)],
                   [np.sin(theta), np.cos(theta), 0],
                   [-np.sin(phi)*np.cos(theta), np.sin(phi)*np.sin(theta), np.cos(phi)]])

print(rot_mat@np.array([[0],
                        [0],
                        [1]]))

def rotationMatrixToEulerAngles(R) :
 
    #assert(isRotationMatrix(R))
 
    sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
 
    singular = sy < 1e-6
 
    if  not singular :
        x = math.atan2(R[2,1] , R[2,2])
        y = math.atan2(-R[2,0], sy)
        z = math.atan2(R[1,0], R[0,0])
    else :
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0
 
    return np.array([x, y, z])

print(180*np.array(rotationMatrixToEulerAngles(rot_mat))/np.pi)