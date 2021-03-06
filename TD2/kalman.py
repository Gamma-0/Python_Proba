from math import *
import pylab as plt
import numpy as np
from matplotlib import animation

# time step
dt = 0.1


# motion uncertainty
R = np.matrix([[1., 0., 0., 0.],
               [0., 1., 0., 0.],
               [0., 0., 1., 0.],
               [0., 0., 0., 1.]])

# initial uncertainty
P =  np.matrix([[5.,0.,0.,0.],
             [0.,5.,0.,0.],
             [0.,0.,100.,0.],
             [0.,0.,0.,100.]])

# Modification 1
# next state function
F=  np.matrix([[1.,0.,dt,0.],
             [0.,1.,0.,dt],
             [0.,0.,1.,0.],
             [0.,0.,0.,1.]])

# measurement function
H =  np.matrix([[1.,0.,0.,0.],
             [0.,1.,0.,0.]])

# measurement uncertainty
Q =  np.matrix([[1.,0.],
             [0.,1.]])

# identity matrix
I =  np.eye(P.shape[0])

# display settings
scale =0.2
xmax = 75
ymax = 75

#compute approximate values of a gaussian distribution
def bin_matrix(x,P):
    M = np.zeros((xmax,ymax))
    sigma = plt.det(P)
    d_pos = np.zeros((P.shape[0],1))
    P_inv = np.linalg.inv(P)
    sum1=0
    for i in range(xmax):
        for j in range(ymax):
            d_pos[0,0] = x[0]-(i*scale)
            d_pos[1,0] = x[1]-(j*scale)
            exp_value = -0.5*(d_pos.transpose()*P_inv*d_pos)
            M[i,j] = 1./(np.sqrt(2 * np.pi*sigma)) * np.exp( exp_value)
            sum1=sum1+ M[i,j]
    for i in range(xmax):
        for j in range(ymax):
            M[i,j]= M[i,j]/sum1
    return M


# compute position (new_x) and uncertainty (new_P) after movement
def move(x, P):
    # Modification 2
    new_x = F * x + u
    new_P = F *  P * np.transpose(F) + R
    return (new_x,new_P)


# compute position (new_x) and uncertainty (new_P) after sensing.
# Z: measurements
def sense(x,P,Z):
    # Modification 3
    Y = Z - (H*x);
    S = H * P * np.transpose(H) + Q
    K = P * np.transpose(H) * np.linalg.inv(S)
    new_x = x + (K * Y)
    new_P = (I - (K * H)) * P;
    return (new_x,new_P)

def filter(x, P, measurements):
    plt.ion()
    l=len(measurements)
    p = bin_matrix(x,P)
    im = plt.imshow(p)
    plt.pause(1)
    for n in range(l):
        # prediction
        (x,P) = move(x,P)
        #plot probabilities after movement
        p = bin_matrix(x,P)
        im = plt.imshow(p)
        plt.pause(0.1)

        # measurement update
        Z = np.matrix([measurements[n]]).transpose()
        (x,P) = sense(x,P,Z)
        #plot probabilities after sensing
        p = bin_matrix(x,P)
        im = plt.imshow(p)
        plt.pause(0.1)

    plt.ioff()
    return [x,P]

def handle_test_case(measurements,initial_xy,final_position):
    x = np.matrix([[initial_xy[0]], [initial_xy[1]], [0.], [0.]])
    res = filter(x, P,measurements)
    filtered_position   = np.array(res[0]).T[0]
    filtered_covariance = np.array(res[1])
    print "-- Estimated position   :", filtered_position
    print "-- Real position        :", final_position
    print "-- Position error       :", np.linalg.norm(final_position-
                                               filtered_position)
    print "-- Estimated covariance :", np.linalg.norm(filtered_covariance)

################################################################
# Test cases
################################################################
print "Test case 1 (4-dimensional example, error-free measurements)"
#u : [x,y,vx,vy]
u = np.matrix([[0], [0], [0.], [0.]])
measurements = [[5., 10.], [6., 8.], [7., 6.], [8., 4.], [9., 2.], [10., 0.]]
initial_xy = [4., 12.]
final_position = np.array([10.,0.,10.,-20.])
handle_test_case(measurements,initial_xy,final_position)


################################################################
print "Test case 2 (4-dimensional example, errors on measurements and initial conditions)"
#u : [x,y,vx,vy]
u = np.matrix([[0], [0], [0.], [0.]])
measurements = [[5.5, 10.], [6.5, 8.3], [7., 5.4], [6.5, 4.2], [9.3, 1.5], [10, 0.5]]
initial_xy = [4., 11.]
final_position = np.array([10.,0.,10.,-20.])
handle_test_case(measurements,initial_xy,final_position)


##############################################################
print "Test case 3 (4-dimensional example, errors and robot acceleration)"
#u : [x,y,vx,vy]
# Modification 5
u = np.matrix([[0], [0], [10.], [-5.]])
measurements = [[5., 11.], [4., 12.5], [4., 13.5], [5., 14.], [7., 14.], [10., 13.5]]
initial_xy = [7., 9.]
final_position = np.array([10,13.5,40.,-10.])

handle_test_case(measurements,initial_xy,final_position)
