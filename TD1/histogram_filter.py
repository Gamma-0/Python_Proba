import numpy as np
import pylab as plt
import time


#retourne une distribution de probabilite uniforme p sur une grille de taille h w
def init_positions(h,w):
    positions = np.zeros((h,w))
    # TODO Question 1
    p = (1.0 / (h*w));
    for i in range(h):
        for j in range(w):
            positions[i,j] = p;
    return(positions)


#met a jour les probabilites de positions du robot (positions) suivant la decision de mouvement du robot (motion) et sa chance de reussir le deplacement p_move
def move(positions,motion):
    (h,w) = positions.shape
    new_positions = np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            # TODO Question 2
            new_positions[i,j]=0#positions[i,j]
    for i in range(h):
        for j in range(w):
            if (i-motion[0] >= 0 and i-motion[0] <h and j-motion[1] >= 0 and j-motion[1] <w):
                #new_positions[i+motion[0],j+motion[1]]+=positions[i,j]*p_move # Se deplacer
                #new_positions[i,j]-=positions[i,j]*p_move # rester sur place
                new_positions[i,j] =  positions[(i-motion[0])%h,(j-motion[1])%w]*p_move
            else:
                new_positions[i,j] = positions[(i)%h,(j)%w]*(1-p_move)
    return(new_positions)


#met a jour la mesure de probabilite de position du robot (positions) suivant la valeur mesuree par les capteurs (measurement) et la fiabilite du capteur (sensor_right)
def sense(positions,measurement):
    (h,w) = positions.shape
    new_positions = np.zeros((h,w))
    sum=0.0
    for i in range(h):
        for j in range(w):
            # TODO Question 3
            new_positions[i,j]=positions[i,j]
            if (colors[i][j] == measurement):
                new_positions[i,j] = positions[i,j]*sensor_right
            else:
                new_positions[i,j] = positions[i,j]*(1.0-sensor_right)
            sum+=new_positions[i,j];
    #print sum
    if (sum > 0):
        for i in range(h):
            for j in range(w):
                new_positions[i,j] = new_positions[i,j]/sum
    return(new_positions)

# applique le filtre a histogramme pour chacun des mouvements du robot
def filter(positions, motions, measurements):
    plt.ion()
    l=len(motions)
    for i in range(l):
        positions = move(positions,motions[i])
        positions = sense(positions,measurements[i])
        #affiche les probabilites de position du robot a la fin de la phase de mesure
        im = plt.imshow(positions,interpolation='nearest')
        plt.pause(1)
    return(positions)

#lance le filtre sur le jeu de donnee fourni, et affiche la
#position du robot estimee par le filtre
def handle_test_case(colors, motions, measurements):
    h = len(colors)
    w = len(colors[0])
    positions = init_positions(h,w)
    #effectue la mise a jour des probabilites de position du robot
    positions = filter(positions, motions, measurements)
    print positions
    ind = np.argmax(positions)
    x = ind / w
    y = ind - w*x
    print "-- Maximal probability :", positions[x,y]
    print "-- Inferred position   :", x, ",", y

################################################################
# TESTS
################################################################

print "Test case 1"

#couleur de chaque position de la grille
colors = [['red', 'red', 'red', 'red' , 'red','red', 'green', 'red', 'red' , 'red'],
          ['red', 'red', 'red', 'red', 'red','red', 'red', 'green', 'orange' , 'red'],
          ['red', 'red', 'red', 'green', 'red','red', 'red', 'red', 'red', 'red'],
          ['red', 'red', 'red', 'red', 'red','red', 'red', 'red', 'red', 'red']]

#mouvements effectues
motions = [[0,0],[0,1],[1,0],[1,0],[0,1],[-1,0],[1,0],[0,0],[0,1]]

#valeurs observee au cours du mouvement
measurements = ['green', 'red', 'green' ,'green', 'orange','green','green','orange','red']

#probabilite que la mesure du senseur soit fiable
sensor_right = 1
#probabilite que le mouvement demande soit effectue
p_move = 0.8

handle_test_case(colors, motions, measurements)
