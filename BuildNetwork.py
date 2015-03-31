from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
#classification
from pybrain.datasets import ClassificationDataSet 
from pybrain.utilities import percentError
from pybrain.structure.modules import SoftmaxLayer
#graphical
from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal


net = buildNetwork(3,3,3,3,1, bias = True) # possible position combo of player1- random - suggested move
ds = SupervisedDataSet(3,1) # position combo of player1 in 1 game - game result


#input neurons
#dictInput = {}
#for i in range(0,8):
    #for j in range(0,8):
        #if j!=i:
            #for k in range(0,8):
                #if k!=j and k!=i:
                    #dictInput[100*i+10*j+k] = 0

#get training set: combo + result 
targetFile = open('data.txt','r') 
for line in targetFile.readlines():
    data = [int(x) for x in line.strip()if x!='']
    position = ""
    for i in range (0,8):
        if (data[i] == 1):
            position = position + str(i)
        result = data[9]
    if position<3:
        print "Error!"
    #find 3-position combo in "position"(with various length) and match to neurons
    for i in range(0,len(position)):
         for j in range(i,len(position)):
            if j!=i:
                for k in range(j,len(position)):
                    if k!=j and k!=i:
                        ds.addSample((int(position[i]),int(position[j]),int(position[k])),(result,))

#------------TRAIN-----------------
trainer = BackpropTrainer(net, ds)
trainer.train()
#trainer.trainUntilConvergence()
